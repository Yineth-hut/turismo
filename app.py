
from urllib import response
from flask import Flask, render_template, request,redirect,url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required,current_user
from flask_wtf.csrf import CSRFProtect
from config import config
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash
from random import sample


# Models:
from models.ModeloUsuario import ModeloUsuario

# Entities:
from models.entities.Usuario import Usuario

app = Flask(__name__)
db = MySQL(app)
csrf = CSRFProtect()
login_manager_app = LoginManager(app)



@login_manager_app.user_loader
def load_user(id):
    return ModeloUsuario.get_by_id(db, id)

#Para subir archivo tipo foto al servidor
import os
from werkzeug.utils import secure_filename 

@app.route('/homePage')
def homePage():
        query ="SELECT * FROM user"
        cursor=db.connection.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        print(row)
        return 'homePage'


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        usuario = Usuario(0,"", request.form['correo_Usuario'], request.form['contraseña_Usuario'])
        logged_user = ModeloUsuario.login(db, usuario)
        if logged_user != None:
            if logged_user.contraseña_Usuario:
                login_user(logged_user)
                return redirect(url_for('admin'))
            else:
                flash("Contraseña Incorrecta...")
                return render_template('auth/login.html')
        else:
            flash("Usuario No Encontrado...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
def inicio():
    
    return render_template('home.html')



@app.route('/singup')
def singup():
    
    return render_template('auth/singUp.html')

@app.route('/register', methods=["POST"])
def register():
    if request.method=="POST":
        contraseña=request.form['pass']

        texto_encriptado1 = generate_password_hash(contraseña)
        name=request.form['nombre']
        correo=request.form['correo']
        contraseñaE=texto_encriptado1
        query =f"INSERT INTO usuario(nombre_Usuario,correo_Usuario,contraseña_Usuario) VALUES('{name}','{correo}','{contraseñaE}')"
        cursor=db.connection.cursor()
        cursor.execute(query)
        db.connection.commit()
        return redirect(url_for('login'))
        
    else:
        return "nooooooo"   

@app.route('/formularioCentrosR')
@login_required
def formulario():
    return render_template('formlarioCentrosR.html')

@app.route('/registerCentrosR', methods=["POST"])
def registerCentrosR():
    if request.method=="POST":
        nombre=request.form['nombre']
        direccion=request.form['direccion']
        descripcion=request.form['descripcion']
        sacerdote=request.form['sacerdote']
        contacto=request.form['contacto']
        file = request.files['imagen'] #recibiendo el archivo
        nuevoNombreFile = recibeFoto(file) #Llamado la funcion que procesa la imagen
        archivo = request.files['horario'] #recibiendo el archivo
        nuevoNombreHorario = recibeFoto(archivo) #
        usuario_Id=current_user.id
        cursor=db.connection.cursor()
        query =f"INSERT INTO centrosreligiosos(nombre_Centro,direccion_Centro,descipcion_Centro,nombreSacerdote_Centro,contacto_Centro,imagen_Centro,horario_Centro,usuario_Id) VALUES('{nombre}','{direccion}','{descripcion}','{sacerdote}','{contacto}','{nuevoNombreFile}','{nuevoNombreHorario}',{usuario_Id})"
        cursor=db.connection.cursor()
        cursor.execute(query)
        db.connection.commit()
        return redirect(url_for('admin'))
        
    else:
        return "nooooooo"


@app.route('/formularioActividadesR')
@login_required
def formularioActividadesR():
    return render_template('formularioActividadesR.html')

@app.route('/registerActividadesR', methods=["POST"])
def registerActividadesR():
    if request.method=="POST":
        nombre=request.form['nombre']
        lugar=request.form['lugar']
        descripcion=request.form['descripcion']
        contacto=request.form['contacto']
        file = request.files['imagen'] #recibiendo el archivo
        nuevoNombreFile = recibeFoto(file) #Llamado la funcion que procesa la imagen
        archivo = request.files['programacion'] #recibiendo el archivo
        programacion = recibeFoto(archivo) #
        usuario_Id=current_user.id
        cursor=db.connection.cursor()
        query =f"""INSERT INTO actividadesreprecentativas(nombre_Actividad,lugar_Actividad,descipcion_Actividad,
        contacto_Actividad,imagen_Actividad,programacion_Actividad,usuario_Id) 
        VALUES('{nombre}','{lugar}','{descripcion}','{contacto}','{nuevoNombreFile}',
        '{programacion}',{usuario_Id})"""
        cursor=db.connection.cursor()
        cursor.execute(query)
        db.connection.commit()
        return redirect(url_for('admin'))
        
    else:
        return "nooooooo"

@app.route('/formularioHotel')
@login_required
def formularioHotel():
    return render_template('formularioHoteles.html')

@app.route('/registerHotel', methods=["POST"])
def registerHotel():
    if request.method=="POST":
        nombre=request.form['nombre']
        direccion=request.form['direccion']
        descripcion=request.form['descripcion']
        contacto=request.form['contacto']
        file = request.files['imagen'] #recibiendo el archivo
        nuevoNombreFile = recibeFoto(file) #Llamado la funcion que procesa la imagen
        archivo = request.files['horarios'] #recibiendo el archivo
        horarios = recibeFoto(archivo) #
        servicios = request.files['servicios'] #recibiendo el archivo
        servicio = recibeFoto(servicios) 
        usuario_Id=current_user.id
        cursor=db.connection.cursor()
        query =f"""INSERT INTO hoteles(nombre_hotel,direccion_hotel,descipcion_hotel,
        contacto_hotel,imagen_hotel,horarios_hotel,servicios_hotel,usuario_Id) 
        VALUES('{nombre}','{direccion}','{descripcion}','{contacto}','{nuevoNombreFile}',
        '{horarios}','{servicio}',{usuario_Id})"""
        cursor=db.connection.cursor()
        cursor.execute(query)
        db.connection.commit()
        return redirect(url_for('admin'))
        
    else:
        return "nooooooo"

@app.route('/formularioSitio')
@login_required
def formularioSitio():
    return render_template('formularioSitio.html')

@app.route('/registerSitio', methods=["POST"])
def registerSitio():
    if request.method=="POST":
        nombre=request.form['nombre']
        direccion=request.form['direccion']
        descripcion=request.form['descripcion']
        contacto=request.form['contacto']
        file = request.files['imagen'] #recibiendo el archivo
        nuevoNombreFile = recibeFoto(file) #Llamado la funcion que procesa la imagen
        archivo = request.files['horarios'] #recibiendo el archivo
        horarios = recibeFoto(archivo) #
        servicios = request.files['planes'] #recibiendo el archivo
        servicio = recibeFoto(servicios) 
        usuario_Id=current_user.id
        cursor=db.connection.cursor()
        query =f"""INSERT INTO sitiosturisticos(nombre_sitiosT,direccion_sitiosT,descipcion_sitiosT,
        contacto_sitiosT,imagen_sitiosT,horarios_sitiosT,planes_sitiosT,usuario_Id) 
        VALUES('{nombre}','{direccion}','{descripcion}','{contacto}','{nuevoNombreFile}',
        '{horarios}','{servicio}',{usuario_Id})"""
        cursor=db.connection.cursor()
        cursor.execute(query)
        db.connection.commit()
        return redirect(url_for('admin'))
        
    else:
        return "nooooooo"
    
@app.route('/formularioRestaurantes')
@login_required
def formularioRestaurantes():
    return render_template('formularioRestaurantes.html')

@app.route('/registerRestaurantes', methods=["POST"])
def registerRestaurantes():
    if request.method=="POST":
        nombre=request.form['nombre']
        direccion=request.form['direccion']
        descripcion=request.form['descripcion']
        contacto=request.form['contacto']
        file = request.files['imagen'] #recibiendo el archivo
        nuevoNombreFile = recibeFoto(file) #Llamado la funcion que procesa la imagen
        archivo = request.files['horarios'] #recibiendo el archivo
        horarios = recibeFoto(archivo) #
        desayunos = request.files['desayunos'] #recibiendo el archivo
        desayuno = recibeFoto(desayunos) 
        almuerzos = request.files['almuerzos'] #recibiendo el archivo
        almuerzo = recibeFoto(almuerzos)#
        postres = request.files['postres'] #recibiendo el archivo
        postre= recibeFoto(postres)
        usuario_Id=current_user.id
        cursor=db.connection.cursor()
        query =f"""INSERT INTO restaurantes(nombre_restaurante,direccion_restaurante,descipcion_restaurante,
        contacto_restaurante,imagen_restaurante,horarios_restaurante,cartaDesayuno_restaurante,cartaAlmuerzo_restaurante,
        cartaPostres_restaurante,usuario_Id) 
        VALUES('{nombre}','{direccion}','{descripcion}','{contacto}','{nuevoNombreFile}',
        '{horarios}','{desayuno}','{almuerzo}','{postre}',{usuario_Id})"""
        cursor=db.connection.cursor()
        cursor.execute(query)
        db.connection.commit()
        return redirect(url_for('admin'))
        
    else:
        return "nooooooo"
    
@app.route('/admin')
@login_required
def admin():
    cursor=db.connection.cursor()
    cursor.execute("SELECT * FROM centrosreligiosos")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()

    cursor=db.connection.cursor()
    cursor.execute("SELECT * FROM restaurantes")
    myresultado = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObjecto = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresultado:
        insertObjecto.append(dict(zip(columnNames, record)))
    cursor.close()

    cursor=db.connection.cursor()
    cursor.execute("SELECT * FROM hoteles")
    myresultados = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObjectos = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresultados:
        insertObjectos.append(dict(zip(columnNames, record)))
    cursor.close()

    cursor=db.connection.cursor()
    cursor.execute("SELECT * FROM sitiosturisticos")
    myresultados2 = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObjectos2 = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresultados2:
        insertObjectos2.append(dict(zip(columnNames, record)))
    cursor.close()

    cursor=db.connection.cursor()
    cursor.execute("SELECT * FROM actividadesreprecentativas")
    myresultados1 = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObjectos1 = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresultados1:
        insertObjectos1.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('admin.html', data=insertObject, dato=insertObjecto, datos=insertObjectos,datos1=insertObjectos1,datos2=insertObjectos2)

@app.route('/delete/<string:id>')
def delete(id):
    cursor=db.connection.cursor()
    sql = "DELETE FROM centrosreligiosos WHERE id_Centro=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.connection.commit()
    return redirect(url_for('admin'))

@app.route('/deleteR/<string:id>')
def deleteR(id):
    cursor=db.connection.cursor()
    sql = "DELETE FROM restaurantes WHERE id_restaurante=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.connection.commit()
    return redirect(url_for('admin')) 


@app.route('/deleteH/<string:id>')
def deleteH(id):
    cursor=db.connection.cursor()
    sql = "DELETE FROM hoteles WHERE id_hotel=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.connection.commit()
    return redirect(url_for('admin')) 

@app.route('/deleteS/<string:id>')
def deleteS(id):
    cursor=db.connection.cursor()
    sql = "DELETE FROM sitiosturisticos WHERE id_sitiosT=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.connection.commit()
    return redirect(url_for('admin')) 

@app.route('/deleteA/<string:id>')
def deleteA(id):
    cursor=db.connection.cursor()
    sql = "DELETE FROM sitiosturisticos WHERE id_sitiosT=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.connection.commit()
    return redirect(url_for('admin')) 

@app.route('/home')
def home():
    return render_template('home.html')


def recibeFoto(file):
    print(file)
    basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
    filename = secure_filename(file.filename) #Nombre original del archivo

    #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
    extension           = os.path.splitext(filename)[1]
    nuevoNombreFile     = stringAleatorio() + extension
    #print(nuevoNombreFile)
        
    upload_path = os.path.join (basepath, 'static/fotos_turismo', nuevoNombreFile) 
    file.save(upload_path)

    return nuevoNombreFile

def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio


def status_401(error):
    return redirect(url_for('login'))


def status_404(error):
    return "<h1>Página no encontrada</h1>", 404





if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
