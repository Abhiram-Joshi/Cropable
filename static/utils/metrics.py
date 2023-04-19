from tensorflow.keras.models import load_model
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import numpy as np


classifier = load_model("model.h5")

# test_set = test_datagen.flow_from_directory('./Dataset/test', target_size = (128, 128), batch_size = 3, class_mode = 'categorical')

# scores = classifier.evaluate_generator(test_set)
# print("Test Accuracy: %.2f%%" % (scores[1]*100))

train_datagen = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)


valid_set = test_datagen.flow_from_directory('./Dataset/val', target_size = (128, 128), batch_size = 3, class_mode = 'categorical')

testing_set = train_datagen.flow_from_directory('./Dataset/test', target_size = (128, 128), batch_size = 6, class_mode = 'categorical')

training_set = train_datagen.flow_from_directory('./Dataset/train', target_size = (128, 128), batch_size = 6, class_mode = 'categorical')

history = classifier.fit_generator(training_set, steps_per_epoch = 20, epochs = 50, validation_data = valid_set)

accuracy = history.history['val_accuracy'][-1]
print('Validation accuracy:', accuracy)


# Make predictions on testing data
predictions = classifier.predict_generator(training_set)
y_pred = np.argmax(predictions, axis=1)

# Get true labels
y_true = training_set.classes

# Generate confusion matrix
cm = confusion_matrix(y_true, y_pred)

print("Confusion matrix:")
print(cm)

# Generate classification report
report = classification_report(y_true, y_pred, target_names=training_set.class_indices.keys())

print("Classification report:")
print(report)

loss, accuracy = classifier.evaluate(x_test, y_test, verbose=1)
loss_v, accuracy_v = classifier.evaluate(x_validate, y_validate, verbose=1)
print("Validation: accuracy = %f  ;  loss_v = %f" % (accuracy_v, loss_v))
print("Test: accuracy = %f  ;  loss = %f" % (accuracy, loss)) 

# plt.plot(history.history['accuracy'])
# plt.plot(history.history['val_accuracy'])
# plt.title('Model Accuracy')
# plt.ylabel('Accuracy')
# plt.xlabel('Epoch')
# plt.legend(['Training', 'Validation'], loc='lower right')