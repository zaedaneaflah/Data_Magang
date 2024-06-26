import streamlit as st
import pandas as pd

# Function to login
def login():
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    return username, password

# Function to check login
def authenticate(username, password):
    # Here you can add authentication logic
    # For example, checking if the username and password match what is predefined
    # or checking with a user database.
    # For this example purpose, we'll use a simple authentication.
    if username == "admin" and password == "admin123":
        return True
    else:
        return False

# Main function to display the homepage
def main():
    st.title("Aplikasi Pendataan Magang")

    # Display login form
    username, password = login()

    # Perform authentication
    if authenticate(username, password):
        st.success("Login berhasil!")

        # Create an empty DataFrame to store internship data
        df = pd.DataFrame(columns=["No", "Nama Lengkap", "Tempat Magang", "Durasi Magang (bulan)"])
        
        # Display input form for internship data
        st.header("Input Data Magang")
        nama_lengkap = st.text_input("Nama Lengkap:")
        tempat_magang = st.text_input("Tempat Magang:")
        durasi_magang = st.number_input("Durasi Magang (bulan):", min_value=1, value=1)
        
        if st.button("Kirim"):
            # Add internship data to the DataFrame
            new_entry = pd.DataFrame({"No": [len(df) + 1], "Nama Lengkap": [nama_lengkap], "Tempat Magang": [tempat_magang], "Durasi Magang (bulan)": [durasi_magang]})
            df = pd.concat([df, new_entry], ignore_index=True)
            st.success(f"Data Magang {nama_lengkap} berhasil ditambahkan.")

        # Display internship data table
        st.header("Data Magang")
        st.table(df.style.set_properties(**{'text-align': 'center'}).set_table_styles([{'selector': 'td', 'props': [('text-align', 'center')]}]))

    else:
        st.error("Username atau password salah.")

if __name__ == "__main__":
    main()



