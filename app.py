import cv2
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision


def dashboard():
    img = None
    st.write("### Banana Ripeness Detection System")
    cam_tab, result_tab = st.tabs(["Camera", "Results"])

    with cam_tab:
        img = st.camera_input("Take picture of banana")

        if img:
            st.success("Image captured Successfully. Click on the [Result] tab")
            img = img

    with result_tab:
        if img:
            img, object_count, category_list = banana_model(img)
            banana_count = {
            "banana_underripe": 0,
            "banana_barely_ripe": 0,
            "banana_ripe": 0,
            "banana_very_ripe": 0,
            "banana_overripe": 0
        }

            st.image(img)
            if not category_list:
                st.error("Banana not detected, please go to the '"'Camera'"' tab and take a picture")
            st.divider()
            c1, c2, c3, c4, c5 = st.columns([1,1,1,1,1])

            for i in category_list:
                if i in banana_count:
                    banana_count[i] += 1

            banana_ripeness_list = ["Underripe Banana","Barely Ripe Banana", "Ripe Banana", "Very Ripe Banana", "Overripe Banana"]
            c_list = [c1, c2, c3, c4, c5]

            for idx, i in enumerate(banana_count):
                c_list[idx].write(f":orange[{banana_count[i]}/{object_count}] {banana_ripeness_list[idx]}")


            banana_colors = ["#93C572","#F8DE7E", "#FFFF00", "#E4D00A", "#8B8000"]
            bananas = ['Underripe', 'Barely ripe', 'Ripe', "Very ripe", "Overripe"]
            fig = go.Figure([go.Bar(x=bananas, y=list(banana_count.values()), marker_color=banana_colors)])
            
            st.plotly_chart(fig)

            if banana_count['banana_underripe'] > 0:  
                with st.expander("Underripe Bananas"):
                    st.image("banana_underripe4.jpeg", width=250)
                    st.write("### Nutritional Facts: ")
                    st.markdown("  - Calories: 89")
                    st.markdown("  - Carbohydrates: 22.8 grams")
                    st.markdown("  - Dietary Fiber: 2.6 grams")
                    st.markdown("  - Sugars: 12.2 grams")
                    st.markdown("  - Vitamin C: 8.7 mg (15% of the Daily Value, DV)")
                    st.markdown("  - Vitamin B6: 0.5 mg (26% of DV)")
                    st.markdown("  - Potassium: 422 mg (12% of DV)")

                    st.write("### Health Benefits: ")
                    st.markdown("  - Resistant Starch: Unripe bananas are rich in resistant starch, which acts like dietary fiber. It can aid in digestion, promote a feeling of fullness, and support colon health.")
                    st.markdown("  - Blood Sugar Control: Resistant starch in unripe bananas may help stabilize blood sugar levels.")

                    
                    st.write("### Used in Cooking Recipes: ")
                    st.markdown("  - Used in savory dishes, such as curries or stews, where their starchy nature adds thickness and texture.")


            if banana_count["banana_barely_ripe"] > 0:
                with st.expander("Barely Ripe Bananas"):
                    st.image("banana_barely_ripe1.jpeg", width=250)
                    st.write("### Nutritional Facts: ")
                    st.markdown("  - Calories: 105")
                    st.markdown("  - Carbohydrates: 26.7 grams")
                    st.markdown("  - Dietary Fiber: 3.1 grams")
                    st.markdown("  - Sugars: 14.8 grams")
                    st.markdown("  - Vitamin C: 10.3 mg (17% of DV)")
                    st.markdown("  - Vitamin B6: 0.6 mg (30% of DV)")
                    st.markdown("  - Potassium: 362 mg (10% of DV)")

                    st.write("### Health Benefits: ")
                    st.markdown("  - Vitamins and Minerals: As bananas ripen, they continue to provide essential nutrients like vitamin C, vitamin B6, and potassium.")
                    st.markdown("  - Digestive Health: The soluble fiber in slightly ripe bananas supports healthy digestion.")

                    
                    st.write("### Used in Cooking Recipes: ")
                    st.markdown("  - Work well in salads, adding a slightly sweet and fruity element")
                    st.markdown("  - They can be sliced and added to yogurt or cereal")

            if banana_count["banana_ripe"] > 0: 
                with st.expander("Ripe Bananas"):
                    st.image("banana_ripe5.jpeg", width=250)
                    st.write("### Nutritional Facts: ")
                    st.markdown("  - Calories: 105")
                    st.markdown("  - Carbohydrates: 26.7 grams")
                    st.markdown("  - Dietary Fiber: 3.1 grams")
                    st.markdown("  - Sugars: 14.8 grams")
                    st.markdown("  - Vitamin C: 10.3 mg (17% of DV)")
                    st.markdown("  - Vitamin B6: 0.6 mg (30% of DV)")
                    st.markdown("  - Potassium: 362 mg (10% of DV)")

                    st.write("### Health Benefits: ")
                    st.markdown("  - Digestive Health: Ripe bananas are easier to digest and can help soothe the stomach. They are often recommended for individuals with gastrointestinal issues.")
                    st.markdown("  - Energy: Ripe bananas provide a quick source of natural energy due to their higher sugar content.")
                    st.markdown("  - Vitamin B6: Ripe bananas are a good source of vitamin B6, which supports brain health and cognitive function.")
                    st.markdown("  - Heart Health: The potassium in ripe bananas is associated with maintaining healthy blood pressure levels.")


                    st.write("### Used in Cooking Recipes: ")
                    st.markdown("  - Banana bread, muffins, pancakes, and waffles")
                    st.markdown("  - Add them to smoothies for natural sweetness and creaminess")
                    st.markdown("  - Mash and use as a topping for oatmeal or cereal")

            if banana_count["banana_very_ripe"] > 0: 
                with st.expander("Very Ripe Bananas"):
                    st.image("banana_very_ripe3.jpeg", width=250)
                    st.write("### Nutritional Facts: ")
                    st.markdown("  - Calories: 121")
                    st.markdown("  - Carbohydrates: 31.1 grams")
                    st.markdown("  - Dietary Fiber: 3.5 grams")
                    st.markdown("  - Sugars: 17.3 grams")
                    st.markdown("  - Vitamin C: 14.1 mg (24% of DV)")
                    st.markdown("  - Vitamin B6: 0.7 mg (35% of DV)")
                    st.markdown("  - Potassium: 400 mg (11% of DV)")

                    st.write("### Health Benefits: ")
                    st.markdown("  - Antioxidants: Very ripe bananas have higher levels of antioxidants, which can help protect cells from damage.")
                    st.markdown("  - Digestive Health: Very ripe bananas are even easier to digest and are sometimes recommended for individuals recovering from stomach illnesses.")
                    st.markdown("  - Natural Sweetness: The sugar content in very ripe bananas can satisfy sweet cravings without the need for added sugars.")

                    st.write("### Used in Cooking Recipes: ")
                    st.markdown("  - Best for baking and desserts")
                    st.markdown("  - Exceptionally sweet banana bread, muffins, and cakes")
                    st.markdown("  - Use them to sweeten and moisten recipes like smoothies, pancakes, and oatmeal")
                    st.markdown("  - Mash and use as a natural sweetener in recipes that call for sugar")

            if banana_count["banana_overripe"] > 0:
                with st.expander("Overripe Bananas"):
                    st.image("banana_overripe1.jpeg", width=250)
                    st.write("### Nutritional Facts: ")
                    st.markdown("  - Calories: 121")
                    st.markdown("  - Carbohydrates: 31.1 grams")
                    st.markdown("  - Dietary Fiber: 3.5 grams")
                    st.markdown("  - Sugars: 17.3 grams")
                    st.markdown("  - Vitamin C: 14.1 mg (24% of DV)")
                    st.markdown("  - Vitamin B6: 0.7 mg (35% of DV)")
                    st.markdown("  - Potassium: 400 mg (11% of DV)")

                    st.write("### Health Benefits: ")
                    st.markdown("  - Antioxidants: Very ripe bananas have higher levels of antioxidants, which can help protect cells from damage.")
                    st.markdown("  - Digestive Health: Very ripe bananas are even easier to digest and are sometimes recommended for individuals recovering from stomach illnesses.")
                    st.markdown("  - Natural Sweetness: The sugar content in very ripe bananas can satisfy sweet cravings without the need for added sugars.")

                    st.write("### Used in Cooking Recipes: ")
                    st.markdown("  - Best for baking and desserts")
                    st.markdown("  - Exceptionally sweet banana bread, muffins, and cakes")
                    st.markdown("  - Use them to sweeten and moisten recipes like smoothies, pancakes, and oatmeal")
                    st.markdown("  - Mash and use as a natural sweetener in recipes that call for sugar")

        else:
            st.error("Picture not taken, please go to the '"'Camera'"' tab and take a picture")
            

def banana_model(img):
    base_options = python.BaseOptions(model_asset_path='banana_model3.tflite')
    options = vision.ObjectDetectorOptions(base_options=base_options,
                                        score_threshold=0.25)
    detector = vision.ObjectDetector.create_from_options(options)

    image = cv2.imdecode(np.frombuffer(img.read(), np.uint8), 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_final = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)
    detection_result = detector.detect(img_final)

    image_copy = np.copy(img_final.numpy_view())
    annotated_image, object_count, category_list = visualize(image_copy, detection_result)
    
    return annotated_image, object_count, category_list
    

MARGIN = 10  
ROW_SIZE = 10  
FONT_SIZE = 1
FONT_THICKNESS = 1
banana_colors = {
    "banana_underripe": (147, 197, 114),
    "banana_barely_ripe": (248, 222, 126),
    "banana_ripe": (255, 255, 0),
    "banana_very_ripe": (228, 208, 10),
    "banana_overripe": (139, 128, 0)
}

def visualize(
    image,
    detection_result
) -> np.ndarray:
  category_list = []

  for detection in detection_result.detections:
    
    category = detection.categories[0]
    category_name = category.category_name
    category_list.append(category_name)
    bbox = detection.bounding_box
    start_point = bbox.origin_x, bbox.origin_y
    end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
    cv2.rectangle(image, start_point, end_point, banana_colors[category_name], 3)
    
    probability = round(category.score, 2)
    result_text = category_name + ' (' + str(probability) + ')'
    text_location = (MARGIN + bbox.origin_x,
                     MARGIN + ROW_SIZE + bbox.origin_y)
    cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                FONT_SIZE, banana_colors[category_name], FONT_THICKNESS)
    
    
  object_count = len(category_list)
  return image, object_count, category_list

if __name__ == '__main__':
    dashboard()