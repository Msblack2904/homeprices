import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('homeprices.pkl','rb'))


def predict_price(area):
    input = np.array([[area]]).astype(np.int64)
    prediction =model.predict(input)
    return float(prediction)

def main():
    st.title("Home price prediction")
    area = st.text_input('Area:','type here')
    if st.button("predict the price"):
        output = predict_price(area)
        st.success(f"The price is {output}")

if __name__=='__main__':
    main()

