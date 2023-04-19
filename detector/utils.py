from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

from django.conf import settings

import numpy as np
import os

model = load_model(os.path.join(settings.BASE_DIR, "static", "utils","model.h5"))

def pred_tomato_disease(tomato_plant):
    test_image = load_img(tomato_plant, target_size = (128, 128)) # load image 
    print("@@ Got Image for prediction")
    
    test_image = img_to_array(test_image)/255 # convert image to np array and normalize
    test_image = np.expand_dims(test_image, axis = 0) # change dimention 3D to 4D
    
    result = model.predict(test_image) # predict diseased palnt or not
    print('@@ Raw result = ', result)
    
    pred = np.argmax(result, axis=1)

    if pred==0:
        return (
            "Tomato - Bacteria Spot Disease",
            "Copper fungicides are the most commonly recommended treatment for bacterial leaf spot. Use copper fungicide as a preventive measure after you've planted your seeds but before you've moved the plants into their permanent homes. You can use copper fungicide spray before or after a rain, but don't treat with copper fungicide while it is raining. If you're seeing signs of bacterial leaf spot, spray with copper fungicide for a seven- to 10-day period, then spray again for one week after plants are moved into the field. Perform maintenance treatments every 10 days in dry weather and every five to seven days in rainy weather."
        )
       
    elif pred==1:
        return (
            "Tomato - Early Blight Disease",
            "Tomatoes that have early blight require immediate attention before the disease takes over the plants. Thoroughly spray the plant (bottoms of leaves also) with Bonide Liquid Copper Fungicide concentrate or Bonide Tomato & Vegetable. Both of these treatments are organic."
        )
        
    elif pred==2:
        return (
            "Tomato - Healthy and Fresh",
            "There is no disease on the Tomato leaf.",
        )
        
    elif pred==3:
        return (
            "Tomato - Late Blight Disease",
            "Tomatoes that have early blight require immediate attention before the disease takes over the plants. Thoroughly spray the plant (bottoms of leaves also) with Bonide Liquid Copper Fungicide concentrate or Bonide Tomato & Vegetable. Both of these treatments are organic."
        )
       
    elif pred==4:
        return (
            "Tomato - Leaf Mold Disease",
            "Use drip irrigation and avoid watering foliage. Use a stake, strings, or prune the plant to keep it upstanding and increase airflow in and around it. Remove and destroy (burn) all plants debris after the harvest."
        )
        
    elif pred==5:
        return (
            "Tomato - Septoria Leaf Spot Disease",
            "Removing infected leaves: Remove infected leaves immediately, and be sure to wash your hands and pruners thoroughly before working with uninfected plants. Consider organic fungicide options: Fungicides containing either copper or potassium bicarbonate will help prevent the spreading of the disease. Begin spraying as soon as the first symptoms appear and follow the label directions for continued management.Consider chemical fungicides: While chemical options are not ideal, they may be the only option for controlling advanced infections. One of the least toxic and most effective is chlorothalonil (sold under the names Fungonil and Daconil)."
        )
        
    elif pred==6:
        return (
            "Tomato - Target Spot Disease",
            "Many fungicides are registered to control of target spot on tomatoes. Growers should consult regional disease management guides for recommended products. Products containing chlorothalonil, mancozeb, and copper oxychloride have been shown to provide good control of target spot in research trials"
        )
        
    elif pred==7:
        return (
            "Tomato - Tomoato Yellow Leaf Curl Virus Disease",
            "Inspect plants for whitefly infestations two times per week. If whiteflies are beginning to appear, spray with azadirachtin (Neem), pyrethrin or insecticidal soap. For more effective control, it is recommended that at least two of the above insecticides be rotated at each spraying."
        )
    
    elif pred==8:
        return (
            "Tomato - Tomato Mosaic Virus Disease",
            """There are no cures for viral diseases such as mosaic once a plant is infected. As a result, every effort should be made to prevent the disease from entering your garden.
            1.Fungicides will NOT treat this viral disease.
            2.Plant resistant varieties when available or purchase transplants from a reputable source.
            3.Do NOT save seed from infected crops.
            4.Spot treat with least-toxic, natural pest control products, such as Safer Soap, Bon-Neem and diatomaceous earth, to reduce the number of disease carrying insects.
            5.Harvest-Guard® row cover will help keep insect pests off vulnerable crops/ transplants and should be installed until bloom.
            6.Remove all perennial weeds, using least-toxic herbicides, within 100 yards of your garden plot.
            7.The virus can be spread through human activity, tools and equipment. Frequently wash your hands and disinfect garden tools, stakes, ties, pots, greenhouse benches, etc. (one part bleach to 4 parts water) to reduce the risk of contamination.
            8.Avoid working in the garden during damp conditions (viruses are easily spread when plants are wet).
            9.Avoid using tobacco around susceptible plants. Cigarettes and other tobacco products may be infected and can spread the virus.
            10.Remove and destroy all infected plants (see Fall Garden Cleanup). Do NOT compost."""
        )
        
    elif pred==9:
        return (
            "Tomato - Two Spotted Spider Mite Disease",
            """For control, use selective products whenever possible. Selective products which have worked well in the field include:
            1. bifenazate (Acramite): Group UN, a long residual nerve poison
            2. abamectin (Agri-Mek): Group 6, derived from a soil bacterium
            3. spirotetramat (Movento): Group 23, mainly affects immature stages
            4. spiromesifen (Oberon 2SC): Group 23, mainly affects immature stages

            OMRI-listed products include:

            1. insecticidal soap (M-Pede)
            2. neem oil (Trilogy)
            3. soybean oil (Golden Pest Spray Oil)
            4. With most miticides (excluding bifenazate), make 2 applications, approximately 5-7 days apart, to help control immature mites that were in the egg stage and protected during the first application. Alternate between products after 2 applications to help prevent or delay resistance."""
        )