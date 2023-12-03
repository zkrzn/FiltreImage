# Image Filtering Application

🖼️ This is a Python code that implements an image filtering application using Streamlit. The application allows you to upload an image and apply various image filtering techniques.

## Requirements

- Python 3.x
- numpy
- streamlit
- PIL (Python Imaging Library)
- scipy

## Link 
You can test the application following this link : [https://filtreimage.streamlit.app/](https://filtreimage.streamlit.app/) (Please wake up the application if you find it asleep)

## Usage

1. Save the script in a file, e.g., `image_filtering_app.py`.
2. Run the script using the following command:

   ````shell
   streamlit run image_filtering_app.py
   ```

3. The application will start, and you can access it through the provided URL.
4. Upload an image by clicking on the "Télécharger une image" button.
5. The application will display the original image, along with the filtered images.
6. The filtering options available are:

   - 📊 **Bruit poisson**: Applies poisson noise to the image.
   - 🖼️ **Image filtrée 3x3**: Applies median filtering with a window size of 3x3.
   - 🖼️ **Image filtrée 5x5**: Applies median filtering with a window size of 5x5.
   - 🖼️ **filtre 7x7**: Applies median filtering with a window size of 7x7.
   - 🖼️ **filtre 11x11**: Applies median filtering with a window size of 11x11.

7. The filtered images will be displayed side by side with the original image.

## Contributions

Contributions to this project are welcome. If you have any suggestions or improvements, feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/username/repo/blob/main/LICENSE) file for more information.
