from os import error
import os
import sys
import io
import folium # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
import projectui
from numpy import number
import handlers
from tkinter import messagebox


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Algeria\'s Map')
        self.window_width, self.window_height = 950, 650
        self.setMinimumSize(self.window_width, self.window_height)
        layout = QVBoxLayout()
        self.setLayout(layout)
        coordinate = (28.033886,1.659626)
        m = folium.Map(tiles='Stamen Terrain',zoom_start=6,location=coordinate)
        L=[]
        #m.save(os.path.join(PATH, ".." , "index.html"))
        try:
            for d in projectui.D.values():
                c = handlers.get_lat_lon(d)
                if c !=[None,None]:
                    folium.Marker(c,popup='None').add_to(m)
                    L.append(tuple(c))
        except error:
            print('Impossible')
        # save map data to data object
        if len(L)== 3:
            folium.PolyLine([L[0],L[1],L[2],L[0]],color='red', weight =3,fillColor = 'red').add_to(m)
        else:
            messagebox.showinfo("ALERT","Inserer des images avec gps Exif Info, svp !")
        data = io.BytesIO()
        m.save(data, close_file=False)
        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)
        #folium.Marker([26.48333,8.46667],popup='None').add_to(m)
def main():
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')
    #t = getgeoloc('illizi')
    myApp = MyApp()
    myApp.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')