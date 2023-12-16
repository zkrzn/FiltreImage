import numpy as np
import streamlit as st
from PIL import Image
from scipy import ndimage

# Ajouter un titre pour cette application streamlit et des metadonnées
st.set_page_config(page_title="Application de filtrage médian",
                   page_icon="🧊",
                   initial_sidebar_state="expanded")


def add_noise(image, noise_type="gaussian", noise_level=0.1):
    # Convertir l'image en tableau numpy
    img_array = np.array(image)
    # Ajouter du bruit
    if noise_type == "gaussian":
        img_noise = img_array + noise_level * np.random.randn(*img_array.shape)
    elif noise_type == "s&p":
        img_noise = img_array.copy()
        # Ajouter du bruit sel et poivre
        s_vs_p = 0.5
        amount = 0.004
        num_salt = np.ceil(amount * img_array.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
                for i in img_array.shape]
        img_noise[coords] = 1
        num_pepper = np.ceil(amount * img_array.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
                for i in img_array.shape]
        img_noise[coords] = 0
    elif noise_type == "poisson":
        img_noise = np.random.poisson(img_array / noise_level) * noise_level
    elif noise_type == "speckle":
        img_noise = img_array + img_array * noise_level * np.random.randn(*img_array.shape)

    # Normaliser l'image
    img_noise = np.clip(img_noise, 0, 255)
    img_noise = img_noise.astype(np.uint8)

    return img_noise


def filtrage_median3(image):
    # Convertir l'image en tableau numpy
    img_array = np.array(image)

    # Appliquer le filtrage médian avec une taille de fenêtre de 3x3
    img_filtree = ndimage.median_filter(img_array, size=3)

    return img_filtree

def filtrage_median5(image):
    # Convertir l'image en tableau numpy
    img_array = np.array(image)

    # Appliquer le filtrage médian avec une taille de fenêtre de 5x5
    img_filtree = ndimage.median_filter(img_array, size=5)

    return img_filtree

def filtrage_median7(image):
    # Convertir l'image en tableau numpy
    img_array = np.array(image)

    # Appliquer le filtrage médian avec une taille de fenêtre de 7x7
    img_filtree = ndimage.median_filter(img_array, size=7)

    return img_filtree

def filtrage_median11(image):
    # Convertir l'image en tableau numpy
    img_array = np.array(image)

    # Appliquer le filtrage médian avec une taille de fenêtre de 11x11
    img_filtree = ndimage.median_filter(img_array, size=11)

    return img_filtree

def main():
    # Titre de l'application
    st.title("Application de filtrage médian")

    # Chargement de l'image depuis l'upload
    uploaded_file = st.file_uploader("Télécharger une image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Lecture de l'image
        image = Image.open(uploaded_file)
        img_array = np.array(image)
        #st.write(img_array.shape)
        #st.write(img_array)
        # Affichage de l'image originale et de l'image filtrée côte à côte
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Image originale")
            st.image(image)

        with col2:
            # application de noise poisson
            img_noise = add_noise(image, noise_type="gaussian")
            st.subheader("Bruit gaussian")
            st.image(img_noise)

        with col3:
            # Application du filtrage médian
            img_filtree = filtrage_median3(image)

            st.subheader("Image filtrée 3x3")
            st.image(img_filtree)
            
        
        col4, col5, col6 = st.columns(3)
        with col4:
            img_filtree = filtrage_median5(image)
            st.subheader("Image filtrée 5x5")
            st.image(img_filtree)

        with col5:
            # Application du filtrage médian
            img_filtree = filtrage_median7(image)

            st.subheader("filtre 7x7")
            st.image(img_filtree)
        
        with col6:
            img_filtree = filtrage_median11(img_noise)
            st.subheader("filtre 11x11")
            st.image(img_filtree)

        

if __name__ == "__main__":
    main()