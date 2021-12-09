import os
import shutil

from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

from catalog import app, conn

global files, session, user, data
session = False
user = ''
files = [[], [], []]
data = []

for file_sd in os.listdir('catalog/static/media/books/SD'):
    if file_sd.endswith('.jpg') or file_sd.endswith('.png'):
        files[0].append(f'{file_sd}')
    else:
        break

for file_smp in os.listdir('catalog/static/media/books/SMP'):
    if file_smp.endswith('.jpg') or file_smp.endswith('.png'):
        files[1].append(f'{file_smp}')
    else:
        break

for file_sma in os.listdir('catalog/static/media/books/SMA'):
    if file_sma.endswith('.jpg') or file_sma.endswith('.png'):
        files[2].append(f'{file_sma}')
    else:
        break


@app.route('/')
def home_page():
    return render_template('home.html', files=files, session=session, user=user)


@app.route('/buku', methods=['GET', 'POST'])
def book_page():
    # Menampilkan data
    sql_tampil = "SELECT * FROM buku ORDER BY idbuku DESC"

    cursor_tampil = conn.cursor()
    cursor_tampil.execute(sql_tampil)

    book = cursor_tampil.fetchall()

    if not session:
        return redirect(url_for('login_page'))
    else:
        return render_template('book.html', book=book, session=session, user=user)


@app.route('/buku/ubah', methods=['POST'])
def ubah_buku():
    # Mengubah data
    _idTemp = request.values.get('temp_id')
    _judul = request.values.get('judul')
    _cat = request.values.get('category')
    _price = request.values.get('harga')
    _desc = request.values.get('deskripsi')
    _isbn = request.values.get('isbn')
    _penulis = request.values.get('penulis')
    _size = request.values.get('ukuran')
    _hlmn = request.values.get('hlmn')

    sql_ubah = "UPDATE buku SET kategori=%s, nama=%s, harga=%s, deskripsi=%s, isbn=%s, penulis=%s, ukuran=%s, halaman=%s WHERE idbuku=%s"
    data_ubah = (_cat, _judul, _price, _desc, _isbn, _penulis, _size, _hlmn, _idTemp)
    cursor_ubah = conn.cursor()
    cursor_ubah.execute(sql_ubah, data_ubah)
    conn.commit()

    flash(f'Data berhasil diubah', category='success')
    return redirect(url_for('book_page'))


@app.route('/buku/hapus/<_cat>/<_kdbuku>/<_id>')
def hapus_data(_cat, _kdbuku, _id):
    sql = "DELETE FROM buku WHERE idbuku = %s"
    _data = _id
    _cat = str(_cat).upper()
    cursor = conn.cursor()
    cursor.execute(sql, _data)
    conn.commit()

    os.remove(f'catalog/static/media/books/{_cat}/{_kdbuku}')

    global files
    files = [[], [], []]
    if _cat == 'SD':
        for file_sd_update in os.listdir('catalog/static/media/books/SD'):
            if file_sd_update.endswith('.jpg') or file_sd_update.endswith('.png'):
                files[0].append(f'{file_sd_update}')
            else:
                break
        for file_smp_update in os.listdir('catalog/static/media/books/SMP'):
            if file_smp_update.endswith('.jpg') or file_smp_update.endswith('.png'):
                files[1].append(f'{file_smp_update}')
            else:
                break
        for file_sma_update in os.listdir('catalog/static/media/books/SMA'):
            if file_sma_update.endswith('.jpg') or file_sma_update.endswith('.png'):
                files[2].append(f'{file_sma_update}')
            else:
                break

    flash(f'Data berhasil dihapus', category='success')
    return redirect(url_for('book_page'))


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    _username = request.values.get('username')
    _password = request.values.get('password')

    if request.method == 'POST':
        sql = 'SELECT * FROM admin WHERE username=%s'

        cursor = conn.cursor()
        cursor.execute(sql, _username)
        hasil = cursor.fetchone()
        akun_cek = cursor.rowcount

        if akun_cek != 0 and _username == hasil[2] and _password == hasil[3]:
            global session, user
            session = True
            user = hasil[1]

            flash(f'Anda login sebagai {user}', category='success')
            return redirect(url_for("home_page"))
        elif not hasil:
            flash(f'Akun tidak tersedia', category='danger')
            return redirect(url_for('login_page'))
        else:
            flash(f'Gagal, tolong periksa kembali', category='danger')
            return redirect(url_for("login_page"))
    else:
        return render_template('login.html')


@app.route('/kategori')
def kategori_buku():
    return render_template('kategori.html', session=session, user=user)


@app.route('/kategori/sd')
def buku_sd():
    return render_template('buku_sd.html', files=files, session=session, user=user)


@app.route('/kategori/smp')
def buku_smp():
    return render_template('buku_smp.html', files=files, session=session, user=user)


@app.route('/kategori/sma')
def buku_sma():
    return render_template('buku_sma.html', files=files, session=session, user=user)


@app.route('/desc/sd/<_kdBook>')
def desc_page_sd(_kdBook):
    sql = "SELECT * FROM buku WHERE kd_buku=%s"
    _data = _kdBook
    cursor = conn.cursor()
    cursor.execute(sql, _data)
    book = cursor.fetchone()

    return render_template('deskripsi.html', data=book, url=f"/static/media/books/sd/{book[1]}", session=session,
                           user=user)


@app.route('/desc/smp/<_kdBook>')
def desc_page_smp(_kdBook):
    sql = "SELECT * FROM buku WHERE kd_buku=%s"
    _data = _kdBook
    cursor = conn.cursor()
    cursor.execute(sql, _data)
    book = cursor.fetchone()

    return render_template('deskripsi.html', data=book, url=f"/static/media/books/smp/{book[1]}", session=session,
                           user=user)


@app.route('/desc/sma/<_kdBook>')
def desc_page_sma(_kdBook):
    sql = "SELECT * FROM buku WHERE kd_buku=%s"
    _data = _kdBook
    cursor = conn.cursor()
    cursor.execute(sql, _data)
    book = cursor.fetchone()

    return render_template('deskripsi.html', data=book, url=f"/static/media/books/sma/{book[1]}", session=session,
                           user=user)


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    _judul = request.values.get('judul')
    _cat = request.values.get('category')
    _price = request.values.get('harga')
    _desc = request.values.get('deskripsi')
    _isbn = request.values.get('isbn')
    _penulis = request.values.get('penulis')
    _size = request.values.get('ukuran')
    _hlmn = request.values.get('hlmn')
    f = request.files['file']

    # Cek ketersediaan data
    sql = 'SELECT * FROM buku WHERE idbuku=%s'

    cursor = conn.cursor()
    cursor.execute(sql, f.filename)
    hasil = cursor.fetchone()

    if request.method == 'POST':
        if hasil != 0:
            global data
            data = [f.filename, _cat.upper(), _judul, _price, _desc, _isbn, _penulis, _size, _hlmn]
            f.save(secure_filename(f.filename))

            if _cat == 'sd':
                return redirect(f'/uploader/sd/')
            elif _cat == 'smp':
                return redirect(f'/uploader/smp/')
            elif _cat == 'sma':
                return redirect(f'/uploader/sma/')
            else:
                flash(f'Kategori tidak sesuai', category='warning')
                return redirect(url_for('upload_file'))
        else:
            flash(f'Buku sudah ada', category='warning')
            return redirect(url_for('upload_file'))
    else:
        return render_template('book.html')


@app.route('/uploader/sd/')
def upload_file_sd():
    sql = "INSERT INTO buku VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    cursor = conn.cursor()
    cursor.execute(sql, (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))
    conn.commit()

    shutil.move(f'{data[0]}', f'catalog/static/media/books/SD/')

    global files
    files = [[], [], []]

    for file_sd_update in os.listdir('catalog/static/media/books/SD'):
        if file_sd_update.endswith('.jpg') or file_sd_update.endswith('.png'):
            files[0].append(f'{file_sd_update}')
        else:
            break

    for file_smp_update in os.listdir('catalog/static/media/books/SMP'):
        if file_smp_update.endswith('.jpg') or file_smp_update.endswith('.png'):
            files[1].append(f'{file_smp_update}')
        else:
            break

    for file_sma_update in os.listdir('catalog/static/media/books/SMA'):
        if file_sma_update.endswith('.jpg') or file_sma_update.endswith('.png'):
            files[2].append(f'{file_sma_update}')
        else:
            break

    flash(f'Data berhasil disimpan', category='success')

    return redirect(url_for('book_page'))


@app.route('/uploader/smp/')
def upload_file_smp():
    sql = "INSERT INTO buku VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    cursor = conn.cursor()
    cursor.execute(sql, (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))
    conn.commit()

    shutil.move(f'{data[0]}', f'catalog/static/media/books/SMP/')

    global files
    files = [[], [], []]

    for file_smp_update in os.listdir('catalog/static/media/books/SMP'):
        if file_smp_update.endswith('.jpg') or file_smp_update.endswith('.png'):
            files[1].append(f'{file_smp_update}')
        else:
            break

    flash(f'Data berhasil disimpan', category='success')

    return redirect(url_for('book_page'))


@app.route('/uploader/sma/')
def upload_file_sma():
    sql = "INSERT INTO buku VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    cursor = conn.cursor()
    cursor.execute(sql, (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))
    conn.commit()

    shutil.move(f'{data[0]}', f'catalog/static/media/books/SMA/')

    global files
    files = [[], [], []]

    for file_sma_update in os.listdir('catalog/static/media/books/SMA'):
        if file_sma_update.endswith('.jpg') or file_sma_update.endswith('.png'):
            files[2].append(f'{file_sma_update}')
        else:
            break

    flash(f'Data berhasil disimpan', category='success')

    return redirect(url_for('book_page'))


@app.route('/user', methods=['GET', 'POST'])
def user_page():
    # Menampilkan data
    sql_tampil = "SELECT * FROM admin ORDER BY iduser DESC"

    cursor_tampil = conn.cursor()
    cursor_tampil.execute(sql_tampil)

    admin = cursor_tampil.fetchall()

    if not session:
        return redirect(url_for('login_page'))
    else:
        return render_template('user.html', admin=admin, session=session, user=user)


@app.route('/user/ubah', methods=['POST'])
def user_edit():
    # Mengubah data
    _idTemp = request.values.get('temp_id')
    _username = request.values.get('username')
    _password = request.values.get('password')

    sql_ubah = "UPDATE admin SET username=%s, password=%s WHERE iduser=%s"
    data_ubah = (_username, _password, _idTemp)
    cursor_ubah = conn.cursor()
    cursor_ubah.execute(sql_ubah, data_ubah)
    conn.commit()

    flash(f'Data berhasil diubah', category='success')
    return redirect(url_for('user_page'))


@app.route('/user/tambah', methods=['POST'])
def tambah_user():
    if request.method == 'POST':
        # Menambah data
        _user = request.values.get('pemakai')
        _username = request.values.get('username')
        _password = request.values.get('password')
        _alamat = request.values.get('alamat')

        if len(_user) <= 50 and len(_username) <= 10 and len(_password) <= 10:
            sql = "INSERT INTO admin VALUES (null, %s, %s, %s, %s)"
            _data = (_user, _username, _password, _alamat)

            cursor = conn.cursor()
            cursor.execute(sql, _data)
            conn.commit()

            return redirect(url_for('user_page'))
        else:
            flash(f'Jumlah karakter melebihi batas', category='danger')
            return redirect(url_for('user_page'))
    else:
        return render_template('blog.html')


@app.route('/user/hapus/<_id>/<_user>')
def hapus_user(_id, _user):
    sql = "DELETE FROM admin WHERE iduser = %s"
    _data = _id
    cursor = conn.cursor()
    cursor.execute(sql, _data)
    conn.commit()

    if _user == user:
        return redirect(url_for('logout_session'))

    else:
        return redirect(url_for('user_page'))


@app.route('/logout')
def logout_session():
    global session, user
    session = False
    user = ''

    flash(f'Anda telah keluar', category='warning')
    return redirect(url_for("home_page"))
