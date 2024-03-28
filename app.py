from src.imports import *;
from src.predict import *;

def main():
    
    st.markdown("<h1 style='text-align: center;'>SQLShield Pro</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Guarding Your Data Citadel: A Robust Defense Against SQL Injection Attacks</p>", unsafe_allow_html=True)
    
    user_input = st.text_area("Enter SQL Query:", height=50)

    if st.button("Detect"):
        if not user_input.strip():
            st.warning("Please enter a SQL query.")
        else:
            predicted_class, confidence = predict(user_input)
            if predicted_class == 1:
                st.warning("Prediction: SQL Injection Detected")
            else:
                st.success("Prediction: No SQL Injection Detected")
            
    st.markdown('</div>', unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()
