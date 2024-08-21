# **Brain Tumor MRI Classification and Localization (CS106: CV-RL-DQN)**

## What?

This project focuses on the classification and localization of brain tumors using MRI images. It leverages cutting-edge techniques in Reinforcement Learning (RL) and Deep Q-Networks (DQN) to tackle the challenges of data scarcity in medical imaging. The model not only classifies the presence of a tumor but also predicts the location of the tumor center, providing crucial insights for medical diagnostics.


## Why?

Accurate brain tumor classification and localization are critical for diagnosis and treatment planning in medical practice. However, the scarcity of labeled medical data poses significant challenges for traditional machine learning models. This project aims to address these challenges by exploring and developing novel methodologies that can effectively work with limited data, making it a valuable tool for medical professionals.


## How?

The project is built upon a combination of Machine Learning, Computer Vision, and Reinforcement Learning techniques. Here's a detailed breakdown of the approach:

1. **Problem Definition**: We framed the classification task as a few-shot learning problem, where the model is trained on a limited dataset of MRI images.
   
2. **Deep Q-Network (DQN) with Momentum**: We implemented an advanced version of DQN, incorporating Polyak Averaging (Exponential Moving Average) to improve model stability and performance. The DQN model was trained to predict tumor locations with high accuracy.

3. **Novel Localization Approach**: We proposed a unique method for tumor localization by predicting the tumor center directly, rather than relying on traditional bounding box methods. This approach transformed the localization problem into a regression task with an infinite action space.

4. **Comprehensive Experiments**: We conducted extensive experiments comparing traditional machine learning models (like SVC and KNN) with deep learning models (like VGG16) and our advanced DQN models. The results demonstrated the superior performance of the DQN models, especially in conditions of data scarcity.


## Achievements

- **High Accuracy in Scarce Data**: The Momentum DQN model achieved a test accuracy of up to 99.4%, outperforming traditional models significantly.
  
- **Novel Insights in RL**: We provided new insights into how reinforcement learning can be applied to medical imaging, particularly in scenarios with limited data.

- **Proposed New Directions**: Our research suggests future possibilities, such as a Yolo-style reinforcement learning model and the coordination of multi-agent systems for complex tasks in medical imaging.

---
