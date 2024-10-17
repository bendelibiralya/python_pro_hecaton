# İçeri Aktar
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('page.html')

# Form sonuçları 
@app.route('/main', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # seçilen resmi almak
        selected_image = request.form.get('image-selector')

        # Görev #2. Metni almak
        text_top = request.form.get('textTop')
        text_bottom = request.form.get('textBottom')
        
        # Görev #3. Metnin rengini almak
        selected_color_1 = request.form.get('color-selector-1')
        selected_color_2 = request.form.get('color-selector-2')
        selected_color_3 = request.form.get('color-selector-3','None')

        if selected_color_3 == 'None':
            selected_color_3 = 'transparent'  

        # Görev #3. Metnin konumunu almak
        text_top_y = request.form.get('textTop_y')
        text_bottom_y = request.form.get('textBottom_y')

        return render_template('index.html', 
                               # Seçilen resmi görüntüleme
                               selected_image=selected_image, 

                               # Görev #2. Metni görüntüleme
                               text_top = text_top,
                               text_bottom = text_bottom,

                               # Görev #3. Rengi görüntüleme
                               selected_color_1 = selected_color_1,
                               selected_color_2 = selected_color_2,
                               selected_color_3 = selected_color_3,

                               # Görev #3. Metnin konumunu görüntüleme
                               text_top_y = text_top_y,
                               text_bottom_y = text_bottom_y
                               )
    else:
        # Varsayılan olarak ilk resmi görüntüleme
        return render_template('index.html', selected_image='logo.png')

@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
