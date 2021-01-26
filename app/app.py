import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import LoginManager, UserMixin , login_user, logout_user, login_required,current_user
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import text
from werkzeug.utils import secure_filename
from hashlib import md5
import glob
import hashlib



UPLOAD_FOLDER = 'static/img'#переменная папки для загрузки файлов
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}#ограничение ни тип файлов

login_manager = LoginManager() # создаем экземпляр класса LoginManager  или login_manager = LoginManager(app)

app = Flask(__name__)
application = app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER#добавляем в кофиг

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/films'# подключаемся к базе
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin@192.168.1.83/lab_4'# подключаемся к базе
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False# отключаем Если установлен в True, то Flask-SQLAlchemy будет отслеживать изменения объектов и посылать сигналы

db = SQLAlchemy(app)#создаем экземпляр класса для работы с алхимией
#db = SQLAlchemy(app)#создаем экземпляр класса для работы с алхимией
app.config['SECRET_KEY'] = b'\xd4\x9c6\xe5\xc7\xa5V\xbb\xbbd\xab\x8b3\xc2"d'# ключ для шифрования сессии происходит автоматически






login_manager.init_app(app)# иниц меняем сообщение и категории по умолчанию
login_manager.login_view = 'login'
login_manager.login_message = ' для доступа к данной странице необходима авторизация'
login_manager.login_message_category = 'warning'

#-----------------------функции---------------------------------------------------------
def allowed_file(filename):#ограничение типа загр файла
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def Md6_file(file):#для шиврования получения хеша
    data=file.read()
    return md5(data).hexdigest()

def hash_s(message):# для формирования названия файла
    hash = hashlib.sha1(message.encode("UTF-8")).hexdigest()#
    return hash[:10]


def autor(current_in):# не использую
    if not current_in.is_authenticated:
        return True

    return False

def autor_not_1_2(current_in):# только для авторизированного админа  и модератора
    if  current_in.is_authenticated:
        if not current_in.id==1:
            if not current_in.id==2:
                
                return True

    return False
#--------------------------------------------------ФУНКЦИИ ДЛЯ РАЗГРАНИЧЕНИЯ ПРАВ ДОСТУПА К СТРАНИЦЕ-------------------------------------------------------------------------------------
def autors_1(current_in):# если админ
    if current_in.is_authenticated:# проверяю что пользователь авторизирован
        if current_in.role_id==1:# если это пользователь с ролью 1(администратор)
            return True
       
    return False

def autors_2(current_in):# если mod
    if current_in.is_authenticated:
        if current_in.role_id==2:
            return True
       
    return False
def autors_3(current_in):# если user
    if current_in.is_authenticated:
        if current_in.role_id==3:
            return True
       
    return False

def autors_anon(current_in):# если не зарегистрированный
    if not current_in.is_authenticated:
        return True
       
    return False
 #----------------------------------------------------------------------------------------------------------------------------------------------       
    



#------------------------------------------------ПРЕОБРАЗУЕМ ОЦЕНКУ-----------------------------------------------------
def text_mark(mark_text):
    #5 – отлично (значение по умолчанию),
    ##4 – хорошо,
    #3 – удовлетворительно,
    #2 – неудовлетворительно,
    #1 – плохо,
    #0 – ужасно.
    if mark_text=='отлично':
        return 5
    if mark_text=='хорошо':
        return 4
    if mark_text=='удовлетворительно':
        return 3
    if mark_text=='неудовлетворительно':
        return 2
    if mark_text=='плохо':
        return 1
    if mark_text=='ужасно':
        return 0
    return None
#----------------------------------------------------------------------------------------------------------------------------------------------
#---------------Преобразуем данные с формы селектора в создании фильма-------------------------------------------------------------------------------------------
            

def ganre_text(gan):
    if gan=='боевик':
        return 1
    if gan=='детектив':
        return 2
    if gan=='исторический':
        return 3
    if gan=='комедия':
        return 4
    if gan=='катастрофа':
        return 5
    if gan=='мелодрама':
        return 6 
    if gan=='музыкальный':
        return 7  
    if gan=='триллер':
        return 8
    if gan=='ужасы':
        return 9
    if gan=='фантастиика':
        return 10
    return 1
    



#-------------------------------------------------------------------------------------------------------------


# --------------------------проверяем писал ли пользователь рецензию-----------------------------------------------------------

def rev_not(current_rev):
    
    if current_rev.is_authenticated:# усли пользователь авторизирован

        for ii in db.session.execute('SELECT * FROM `review` ORDER BY `userexam_id` ASC'): # смотрим по базе писал ли он рецензию( есть ли его id)
            if ii.userexam_id==current_rev.id:
                
                return True# усли пользователь писал рецензию то возврашаем истину
    #если пользователь писал рецензию то он есть в таблице userexam_id и не разрешаем рецензировать
        
    return False



#-------------------------------------------------------------------------------



#-------------------таблица многие ко многим(по мануалу)-------------------------------------------




film = db.Table('film_genre',
    db.Column('film_id', db.Integer, db.ForeignKey('film.id_film')),#формирование таблизы многие ко многим в моделе
    db.Column('g_id', db.Integer, db.ForeignKey('genre.id_g'))

)
   

#------------------модель базы данных--------------------------------------------------------------------------------


class Film(db.Model):
    __tablename__='film'

    id_film = db.Column(db.Integer, primary_key=True)
    name_film = db.Column(db.String(50), unique=False, nullable=False)
    descript_film = db.Column(db.Text, unique=False, nullable=False)
    year_film = db.Column(db.String(50), unique=False, nullable=False)
    country = db.Column(db.String(50), unique=False, nullable=False)
    producer = db.Column(db.String(50), unique=False, nullable=False)
    s_writer =db.Column(db.String(50), unique=False, nullable=False)
    actors = db.Column(db.String(250), unique=False, nullable=False)
    duration = db.Column(db.Integer, unique=False, nullable=False)
    poster_id = db.Column(db.Integer, db.ForeignKey('poster.id_poster'))

    def __repr__(self):# способ отображение изменён 
        return '<Film %r>' % self.id_film

class Poster(db.Model):
    __tablename__='poster'
    id_poster = db.Column(db.Integer, primary_key=True)
    name_file = db.Column(db.String(50), unique=False, nullable=False)
    MIME = db.Column(db.String(50), unique=False, nullable=False)
    MD5 = db.Column(db.String(50), unique=False, nullable=False)

    def __repr__(self):# способ отображение изменён 
        return '<Poster %r>' % self.id_poster

class Genre(db.Model):
    __tablename__='genre'
    id_g = db.Column(db.Integer, primary_key=True)
    name_g = db.Column(db.String(50), unique=False, nullable=False)
    film = db.relationship('Film', secondary=film,
        backref=db.backref('genre', lazy='dynamic'))




    def __repr__(self):# способ отображение изменён 
        return '<Genre %r>' % self.id_g

class Review(db.Model):
    __tablename__='review'
    id_rev = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.Integer, db.ForeignKey('film.id_film'))
    userexam_id = db.Column(db.Integer, db.ForeignKey('user_exam.id_userexam'))
    mark = db.Column(db.String(25), unique=False, nullable=False)
    text_r = db.Column(db.Text, unique=False, nullable=False)
    data_r = db.Column(db.DateTime, default = datetime.utcnow) # дата пишется автоматически

    def __repr__(self):# способ отображение изменён 
        return '<Review %r>' % self.id_rev

class Role(db.Model):
    __tablename__='role'
    id_role = db.Column(db.Integer, primary_key=True)
    name_role = db.Column(db.String(50), unique=False, nullable=False)
    descript_role = db.Column(db.Text, unique=False, nullable=False)
    def __repr__(self):# способ отображение изменён 
        return '<Role %r>' % self.id_role

class User_exam(db.Model):
    __tablename__='user_exam'
    id_userexam = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=False, nullable=False)
    hash = db.Column(db.String(250), unique=False, nullable=False)
    s_name = db.Column(db.String(50), unique=False, nullable=False)
    f_name = db.Column(db.String(50), unique=False, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id_role'))

    def __repr__(self):# способ отображение изменён 
        return '<User_exam %r>' % self.id_userexam


class Film_gl(db.Model):
    __tablename__='film_gl'
    id_page = db.Column(db.Integer, primary_key=True)
    name_film = db.Column(db.String(50), unique=False, nullable=False)
    name_g = db.Column(db.String(50), unique=False, nullable=False)
    year_film = db.Column(db.String(50), unique=False, nullable=False)
    count_rev = db.Column(db.Integer, unique=False, nullable=False)
    id_film = db.Column(db.Integer, unique=False, nullable=False)


#--------------------------------------------------------------------------------------------------------------
#---------------------------запрос к базе 1------------------------------------------------------

def Basa1():
    try:
        users_q = db.session.execute('SELECT film.id_film, film.name_film, genre.name_g, review.text_r, review.mark, user_exam.login FROM film JOIN (genre, film_genre, review, user_exam) ON (film.id_film=film_genre.film_id and genre.id_g=film_genre.g_id and film.id_film=review.film_id and review.userexam_id=user_exam.id_userexam)' )

    except:
       flash('Ошибка чтения из базы login','danger') 
    return users_q



#----------------------------------------------------------------------------

#---------------------------запрос к базе для отображения на главной странице------------------------------------------------------

def Basa_g():# формирование ответа на запрос для отображения на главной странице
    try:
        users_g = db.session.execute('SELECT film.name_film, genre.name_g, year_film, count(id_rev), id_film FROM film left JOIN (genre, film_genre) ON (film.id_film=film_genre.film_id and genre.id_g=film_genre.g_id) left join review on film.id_film=review.film_id GROUP BY film.name_film ORDER BY year_film DESC ' )

    except:
       flash('Ошибка чтения из базы ','danger') 
    return users_g

#----------------------------------------------------------------------------

#--------------------------------- функция запрос на заполнение таблицы многие ко многим-----------------------------------------------------------------------
def basa_film_genre(film_id,g_id):

    film_id=str(film_id)
    g_id=str(g_id)
    try:
        sql = text('INSERT INTO film_genre (film_id, g_id) VALUES ('+film_id+','+g_id+')')
        result = db.engine.execute(sql)
    except:
        print('ошибка чтения из базы')
    
    
    
    return None


#--------------------------------------------------------------------------------------------------------


#-----------------------авторизация пользователя  наследуем класс------------------------------------------------------------
class User(UserMixin):# унаследованный от UserMixin в котором реализованы необходимые атрибуты (get_id и тд) вместо отределения вручную
    def __init__(self, user_id, login, password,role_id): # переопределяем метод init принимает др параметры
        super().__init__()# вызываем метод у род класса  UserMixin
        self.id = user_id# проставл значение атрибутов id
        self.login = login# проставл значение атрибутов login
        self.password = password# проставл значение атрибутов password
        self.role_id = role_id# добавляем роль пользователя чтобы разделить права доступа
#---------------------------------------------------------------------------------------------------------------------



#----------------------------------проверяем по сессии кто вошел на сайт--------------------------------------------------

@login_manager.user_loader
def load_user(user_id):# принимаем идентифмкатор текущего пользователя
    try:# это обработчик ошибок чтобы программа не падала
        admin = User_exam.query.filter_by(id_userexam=user_id).first()# user_id это строковая переменная!!!
        
        #Можно использовать и Users.query.get() сразу по id искать 
        usid = admin.id_userexam# из объекти выделяем id оно в базе интеджед

        if usid == int(user_id):# user_id это блин строка переводим и сравниваем
        # передаем данные что и авторизирует пользователя
            return User(admin.id_userexam,admin.login,admin.hash,admin.role_id)# что бы вернуть пользователя нужно создать обьект класса User() и передать ему данные пользователя

    except:# если базы нет или еще какие проблемы выводим кучу ошибок
        db.session.rollback()
        flash('ошибка чтения из базы данных load_user','danger')
        flash('создайте базу данных , таблицу и пользователя admin','danger')

    return None        
#-----------------------------------------------------------------------------------------



#----------------------------------авторизируем пользователя----------------------------------------------------------------------------------------------------
@app.route('/loginform' , methods=('POST','GET'))# авторизуюсь данные из базы\ все работает
def loginform():
    if request.method == 'POST': #если метод POST
        login = request.form.get('login')# сохраняем значение логин
        password = request.form.get('password')#сохраняем значение пароль
        remember_me = request.form.get('remember_me') == 'on'# если галочка стоит то сохраняем True
        if login and password:# если есть логин и пароль 
            try:#обрабатываем ошибки
                admin = User_exam.query.filter_by(login=login).first()#ищем пользователя по логину
                
                adm = admin.hash# берем с объкта хеш парля и логин
                log = admin.login
                rr = admin.role_id
            except:# если ошибка с базой выводим сообщение и выкидываем на главную
                db.session.rollback()
                flash('Ошибка чтения из базы login','danger')
                return redirect(url_for('index'))

            

            if login == log and check_password_hash(adm,password):
                # если логины совпадают( как они могут не совпадать я же по логину искал)
                # то есть логин можно убрать
                # применяем функцию сравнения пароля и хеша если возвращает истину идем дальше
                # создаем экземпляр класса User и передаем ему все данные пользователя


                    user_object = User(admin.id_userexam,admin.login,admin.hash,admin.role_id)
                    
                    login_user(user_object, remember=remember_me)
                #Flask-Login предоставляет функцию login_user(). Она принимает объект пользователя. В случае успеха возвращает True и устанавливает сессию. В противном случае — False.
                    
                    # login_user заносит в сессию информацию о текушем пользователе поэтому Flask определяет авторизирован пользователь или нет
                    flash('вы успешно вошли','success')# вы водим сообщение с категорией 

                    next = request.args.get('next')# из параметра 'next возвращается адрес страницы откуда пришел пользователь

                    return redirect (next or url_for('index')) # перенаправляется на эту страницу  

        flash('ВВедены не верные логин или пароль','danger') #   # вы водим сообщение с категорией 

    return render_template('loginform.html')#
#------------------------------------------------------------------------------------------------------------------

#-------------------------выход из авторизации-------------------------------------------------------------------------------------
@app.route('/logout')# обработчик страницы выхода достаточно перейти на эту страницу и завершается сеанс
def logout():
    logout_user() #logout_user() во Flask-Login завершает сеанс пользователя, удаляя его идентификатор из сессии

    return redirect(url_for('index'))

#----------------------------------------------------------------------------------------------------------------------------------------

# для пагинации на странице применен Внутренний вспомогательный класс, возвращаемый BaseQuery.paginate()
#это утилита работает только с таблицей в базе, поэтому для реализации пагинации : производится запрос в базу с интересующими
#колонками на выходе записывается запрос во вспомогательную таблицу после чего из это таблицы выводится на страницу
# paginate добавляет к экземпляру класса переменные которые позволяют упралять пагинацией на странице
# 
#-----------------------------обработчик главной страницы c с пагинацией фильмов-----------------------------------------------------------------------------------------
@app.route('/film/',methods=['GET'], defaults={"page": 1})
@app.route('/film/<int:page>', methods=['GET'])
def film(page):
    page = page
    per_page = 5
    film_del = {}
    # применяем пагинацию для вывода созданной таблицы в базе
    try:
        users = Film_gl.query.paginate(page,per_page,error_out=False) # для передачи в шаблон и распарсивания таблицы с присоединенными параметрами от утилиты пагинации      
    except:
        flash('ошибка','danger')
    modal=True# устанавливаем флаг молального окна ( не открываться)
    if request.method == 'POST':
        print('11')
    if request.args.get('del', None)!=None:#принимаем нажатие на кнопку удалить
        print(request.args.get('del', None))
        modal=False# если пришшла страница с параметрами?del=  открываем модальное окно статусом модал и ищем по параметру(это айди)фильм
        try:
            film_del = Film.query.filter_by(id_film=request.args.get('del', None)).first()# находим фильм в базе по id для передачи в шаблон    
        except:
            flash('ошибка','danger')
    
    
    return render_template("film.html", users=users, modal=modal,film_del=film_del)

#-----------------------------------------------------------------------------------------------------------------------------

#----------------------------------обработчик добавления фильма---------------------------------------------------------------------------------------------

@app.route('/addfilm',methods=('POST','GET'))
def addfilm():
    if (not (autors_1(current_user)) or autors_anon(current_user)): #  только админ может добавить фильмы
       # чтобы не смещать код в if вместе с функцией применено двойное отрицание
        flash('Для выполнения данного действия необходимо пройти процедуру аутентификации','danger')
        return redirect(url_for('loginform'))

    user={}
    genre={}
    if request.method == 'POST' :# если нажата кнопка


        if 'file' not in request.files:# проверяем наличие файла
            flash('нет файла постера','danger')
            return redirect(request.url)
        file_1 = request.files['file']# считывем файл в переменную
        filename=hash_s(request.form['name_film'])+'.jpg'# формируем имя файла захешированное от имени фильма плюс расштрение
        file_1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))# при помощи save() записываем файл в определенную переменной директорию
        hash_1=Md6_file(file_1)
        print(filename)
        
        
            
            
        try:
            poster_1=Poster(name_file=filename,MIME='file', MD5=hash_1)# из собранныз параметров создаем экземпрляр класса 
            db.session.add(poster_1)# выполняем добавление и комитим
            db.session.commit()
                    #этот запрос можно убрать та как id объекто появляется после комита
            poster_se=Poster.query.filter_by(name_file=filename).first()# забираем этот постер из базы(поскольку нужен его id)
            print('id poster',poster_se.id_poster)
        except:
            db.session.rollback()
            flash('Ошибка добавления в базу данных','danger')

        #здесь проверка на пустые поля в форме
        if request.form['name_film']=='' or request.form['descript_film']=='' or request.form['year_film']=='' or request.form['country']=='' or request.form['producer']==''or request.form['s_writer']=='' or request.form['actors']=='' or request.form['duration']=='':

            flash('Внимание !!!!  Нужно заполнить все поля!!!','danger')
            return redirect(url_for('addfilm'))

        else:  

            try:
                
                # и вот создаем экз класса для записи фильма добавляем в него данные из формы в том числе id постера
                film_add = Film(name_film=request.form['name_film'], descript_film=request.form['descript_film'],year_film= request.form['year_film'],country=request.form['country'],producer= request.form['producer'],s_writer=request.form['s_writer'],actors=request.form['actors'],duration=request.form['duration'],poster_id=poster_se.id_poster   )

                db.session.add(film_add)
                
                db.session.commit()
                basa_film_genre(film_add.id_film,ganre_text(request.form['genre']))# добавляем жанр через в том числе функцию

                print(film_add.id_film)
                flash('фильм добавлен в базу','success')
                
                
            except:
                db.session.rollback()
                flash('Ошибка добавления в базу данных','danger')


        
            

        return redirect(url_for('film', user=user))
    


    return render_template("addfilm.html", user=user,genre=genre)
#---------------------------------------------------------------------------------------------------------------------------------

#-----------------------обработчик редактирования фильма------------------------------------------------------------------------------------------------

@app.route('/editfilm',methods=('POST','GET'))
def editfilm():
    if (not (autors_1(current_user) or autors_2(current_user))) or autors_anon(current_user):#  если вошел админ или мод
       
        flash('Для выполнения данного действия необходимо пройти процедуру аутентификации','danger')
        return redirect(url_for('loginform'))
    
    user={}
    edit_num = request.args.get('edit', None)# смотрим какого  id пользователя редактировать
    print(edit_num)
    if request.method == 'POST':
        if request.form['name_film']=='' or request.form['descript_film']=='' or request.form['year_film']=='' or request.form['country']=='' or request.form['producer']==''or request.form['s_writer']=='' or request.form['actors']=='' or request.form['duration']=='':

            flash('Внимание !!!!  Нужно заполнить все поля!!!','danger')
            return redirect(url_for('addfilm'))
        else:

            try:#находим пользователя по id и меняем все поля на значения из формы
                edit_f=Film.query.get(edit_num)
                edit_f.name_film=request.form['name_film']
                edit_f.descript_film=request.form['descript_film']
                edit_f.year_film=request.form['year_film']
                edit_f.country=request.form['country']
                edit_f.producer=request.form['producer']
                edit_f.s_writer=request.form['s_writer']
                edit_f.actors=request.form['actors']
                edit_f.duration=request.form['duration']
                # комитим
                db.session.commit()

                flash('данные добавлены в базу','success')
            except:
                db.session.rollback()
                flash('Ошибка добавления в базу данных','danger')
        return redirect(url_for('film', user=user))
    try:
        user = Film.query.filter_by(id_film=int(edit_num)).first()# ищем фильм по id и передаем его в шаблон для отображения в окошках ввода данных

    except:
        flash('Ошибка чтния из базы данных','danger')

    return render_template("editfilm.html", user=user)

#--------------------------------------------------------------------------------------------------------------------------

#-------------------------------обработчик просмотра фильма--------------------------------------------------------------------------------------------
@app.route('/viefilm')
def viefilm():
    rev_flag=True
    if rev_not(current_user): # если пользователь писал рецензию не показываем кнопку (меняем флаг)
        rev_flag=False# выключаем кнопку добавить рецензию
    film_u={}
    if request.args.get('look', None)==None:# если просто зашли на страницу и не выбрали фильм
        flash('филм не выбран!! Выберете фильм','danger')
        return redirect(url_for('index'))


    vie_num = request.args.get('look', None)# смотрим какого  id пользователя редактировать
    print(vie_num)
    film_u=Film.query.get(vie_num)
    poster=Poster.query.filter_by(id_poster=film_u.poster_id).first()# находим запись ростера по id
    Foto_pos = poster.name_file# находим имя файла с постером из объекта 
    Foto_pos='img/'+Foto_pos# добавляем путь и перпедаем в шаблон
    print(Foto_pos)

    
    rev= db.session.execute('SELECT * FROM `review`')# из базы берем таблицу с рецензиями и передаем в шаблон для отображения
    
    

    return render_template("viefilm.html", film=film_u,Foto_pos=Foto_pos,rev=rev,rev_flag=rev_flag)

#---------------------------------------------------------------------------------------------------------------------

#-------------------------------обработчик добавления рецензии---------------------------------------------------------------------------
@app.route('/addrev',methods=('POST','GET'))
def addrev():
    if (not (autors_1(current_user) or autors_2(current_user) or autors_3(current_user))) or autors_anon(current_user):#  если вошел админ или мод
       
        flash('Для выполнения данного действия необходимо пройти процедуру аутентификации','danger')
        return redirect(url_for('loginform'))
    user={}
    us_status=True
    us=current_user.role_id
    mon_r=False # статус 
    
    print(current_user.login)
    rev_num = request.args.get('rev', None)#смотрим парамерт строки
    print(rev_num)
    if request.method == 'POST':
        
        print('текст',request.form.get('text_r'))
        print('оценка',request.form.get('mark'))
        print('оценгка2', text_mark(request.form.get('mark')))
        print('пользователь',current_user.id)
        if request.form.get('text_r')=='':# проверяем на пустое поли
            flash('Внимание !!!!  Нужно заполнить все поля!!!','danger')
            return redirect(url_for('addrev'))
        else:

            try:#добавляем в таблицу рецензию
                rev_v = Review(film_id=rev_num, userexam_id=current_user.id, mark= text_mark(request.form.get('mark')),text_r=request.form.get('text_r'))
                db.session.add(rev_v)
                db.session.commit()

                flash('Рецензия добавлена','success')

            except:

                db.session.rollback()
                flash('ошибка добавления в базу','danger')
            return redirect(url_for('index'))

    




    return render_template("addrev.html")

#------------------------------------------------------------------------------------------------------------


#---------------------------------обработчик главной-------------------------------------------------
@app.route('/')
def gl():
    
    #s=Basa_g() стираем таблицу созданную для отображения информации на главной с пагинацией
    delete_film_gl = db.session.execute('TRUNCATE TABLE `film_gl`')# стираем таблицу перед записью
    for r in Basa_g():# выполняем запрос из базы  и проходим по нему записывая в таблицу(ПРОМЕЖЕТОЧНУЮ)для дальнейшего вывода
        try:
        
            db.session.add(Film_gl(name_film =r.name_film, name_g=r.name_g, year_film=r.year_film, count_rev=r[3],id_film=r.id_film))# запись в таблицу результатов запроса basa+g
            db.session.commit()
        except:
            print('ошибка записи')

    return redirect(url_for('film'))
#-------------------------------------------------------------------------------------


#-------------------------------обработчик удаления фильма-----------------------------------------------------------------------------------
@app.route('/delete')
def delete():
    if (not (autors_1(current_user))) or autors_anon(current_user):#  если вошел не админ или анон
       
        flash('Для выполнения данного действия необходимо пройти процедуру аутентификации','danger')
        return redirect(url_for('loginform'))
    

    delet_e = request.args.get('delete', None)#читаем параметр строки с ключем delete 
    print('-----',delet_e )
    if request.args.get('delete', None)!=None:
        try:
            # находим по id фильм
            del_f = Film.query.filter_by(id_film=delet_e).first()
            poster_id_d=del_f.poster_id# находим id постера  на фильм
            poster_f=Poster.query.filter_by(id_poster=poster_id_d).first()# ищем строку с постером
            file_name_poster=poster_f.name_file#  находим имя файла для удаления
            db.session.delete(del_f)
            db.session.commit()# комитим удаление фильма
            print(file_name_poster)
            file_path='static/img/'+file_name_poster# формируем путь к файлу
            os.remove(file_path)#удаляем постер
            
        except:
            print('ошибка')
        try:
            file_path='static/img/'+file_name_poster# формируем путь к файлу
            os.remove(file_path)#удаляем его
        except OSError as e:
            print("Ошибка: %s : %s" % (file_path, e.strerror))# выводим ошибку если например нет такого файла

        flash('фильм удален','success')



    return redirect(url_for('gl'))




#-----------------------------------------------------------------------------------------------------------------------
    
#----------------------обработчик модерации рецензий-------------------------------------------------------------------------------------

@app.route('/modrev')        
def modrev():
    if (not (autors_1(current_user) or autors_2(current_user))) or autors_anon(current_user):#  если вошел админ или мод
       
        flash('Для выполнения данного действия необходимо пройти процедуру аутентификации','danger')
        return redirect(url_for('loginform'))

    if request.args.get('modr', None)!=None:

        mod_num = request.args.get('modr', None)#смотрим парамерт строки
        
        try:
                # находим запись по id и удаляем
            rev_del=Review.query.filter_by(id_rev=mod_num).first()
            db.session.delete(rev_del)
            db.session.commit()
            flash('запись промодерирована','success')
        except:
            print('ошибка')





    return redirect(url_for('gl'))







#-----------------------------------------------------------------------------------------------------------------





#-------------------------загрузки пользователей в базу---------------------------------------------------------------
@app.route('/a')
def a():
    try:

        dd=User_exam(login='admin', hash = generate_password_hash('123'), s_name ='admin', f_name ='adm', role_id = 1)
        db.session.add(dd)
            
        db.session.commit()
            
        flash('пользователь admin добавлен в базу','success')

    except:

        db.session.rollback()
        flash('ошибка добывления в базу','danger')

    return redirect(url_for('index'))






@app.route('/a2')
def a2():
    try:

        #dd=User_exam(login='mod', hash = generate_password_hash('123'), s_name ='модератор', f_name ='модератор', role_id = 2)
        #dd2=User_exam(login='user', hash = generate_password_hash('123'), s_name ='пользователь', f_name ='пользователь', role_id = 3)
        dd5=User_exam(login='user5', hash = generate_password_hash('123'), s_name ='g_ilya', f_name ='j', role_id = 3)
        dd6=User_exam(login='user6', hash = generate_password_hash('123'), s_name ='w_fill', f_name ='g', role_id = 3)
        dd7=User_exam(login='user7', hash = generate_password_hash('123'), s_name ='s_ivan', f_name ='b', role_id = 3)
        dd8=User_exam(login='user8', hash = generate_password_hash('123'), s_name ='f_petr', f_name ='v', role_id = 3)
        db.session.add(dd5)
        db.session.add(dd6) 
        db.session.add(dd7)
        db.session.add(dd8)
        
    
        db.session.commit()
            
        flash('пользователь admin добавлен в базу','success')

    except:

        db.session.rollback()
        flash('ошибка добывления в базу','danger')

    return redirect(url_for('index'))



    #return render_template('index.html', delete_footer=True )


@app.route('/aaggg')
def aa():
    dd=User_exam(login='admin', hash = generate_password_hash('123'), s_name ='admin', f_name ='adm', role_id = 1)
    db.session.add(dd)


    db.session.commit()

    return render_template('index.html' )
#-------------------------------------------------------------------------------------------

@app.route('/')
def index():
    print('123')

    return render_template('index.html' )





#---------------------------------------------------------------------------------





@app.route('/www')
def indexww():

    basa_film_genre(9,6)

    return render_template('index.html' )






if __name__ == "__main__":
    app.run(debug=True)

    
