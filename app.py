from flask import Flask,render_template,request,redirect,url_for
import requests
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        biblia = request.form['nome']
        capitulo = request.form['capitulo']
        return redirect(url_for('biblia',nome=biblia,capitulo=capitulo))
    else:
        return render_template('index.html')
@app.route('/biblia/gn')
def genesis():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    return render_template('gn.html',list=list)
@app.route('/biblia/ex')
def exodo():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    return render_template('ex.html',list=list)
@app.route('/biblia/lv')
def levitico():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
    return render_template('lv.html',list=list)
@app.route('/biblia/nm')
def numeros():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    return render_template('nm.html',list=list)
@app.route('/biblia/dt')
def deuteronomio():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]
    return render_template('dt.html',list=list)
@app.route('/biblia/js')
def josue():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    return render_template('js.html',list=list)
@app.route('/biblia/jz')
def juizes():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    return render_template('jz.html',list=list)
@app.route('/biblia/ru')
def ruth():
    list = [1,2,3,4]
    return render_template('ru.html',list=list)
@app.route('/biblia/1sm')
def samuel():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    return render_template('1sm.html',list=list)
@app.route('/biblia/2sm')
def samuelb():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    return render_template('2sm.html',list=list)
@app.route('/biblia/1rs')
def reis():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    return render_template('1rs.html',list=list)
@app.route('/biblia/2rs')
def reisb():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    return render_template('2rs.html',list=list)
@app.route('/biblia/1cr')
def cronicas():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
    return render_template('1cr.html',list=list)
@app.route('/biblia/2cr')
def cronica():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    return render_template('2cr.html',list=list)
@app.route('/biblia/ed')
def esdras():
    list = [1,2,3,4,5,6,7,8,9,10]
    return render_template('ed.html',list=list)
@app.route('/biblia/ne')
def neemias():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    return render_template('ne.html',list=list)
@app.route('/biblia/et')
def ester():
    list = [1,2,3,4,5,6,7,8,9,10]
    return render_template('et.html',list=list)
@app.route('/biblia/job')
def job():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42]
    return render_template('job.html',list=list)
@app.route('/biblia/sl')
def salmos():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150]
    return render_template('sl.html',list=list)
@app.route('/biblia/pv')
def proverbios():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    return render_template('pv.html',list=list)
@app.route('/biblia/ec')
def eclesiastes():
    list = [1,2,3,4,5,6,7,8,9,10,11,12]
    return render_template('ec.html',list=list)
@app.route('/biblia/ct')
def cantares():
    list = [1,2,3,4,5,6,7,8]
    return render_template('ct.html',list=list)
@app.route('/biblia/is')
def isaias():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66]
    return render_template('is.html',list=list)
@app.route('/biblia/jr')
def jeremias():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
    return render_template('jr.html',list=list)
@app.route('/biblia/lm')
def lamentacoes():
    list = [1,2,3,4,5]
    return render_template('lm.html',list=list)
@app.route('/biblia/ez')
def ezequiel():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]
    return render_template('ez.html',list=list)
@app.route('/biblia/dn')
def daniel():
    list = [1,2,3,4,5,6,7,8,9,10,11,12]
    return render_template('dn.html',list=list)
@app.route('/biblia/os')
def oseias():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    return render_template('os.html',list=list)
@app.route('/biblia/jl')
def joel():
    list = [1,2,3]
    return render_template('jl.html',list=list)
@app.route('/biblia/am')
def amos():
    list = [1,2,3,4,5,6,7,8,9]
    return render_template('am.html',list=list)
@app.route('/biblia/ob')
def obadias():
    list = [1]
    return render_template('ob.html',list=list)
@app.route('/biblia/jn')
def jonas():
    list = [1,2,3,4]
    return render_template('jn.html',list=list)
@app.route('/biblia/mq')
def miqueias():
    list = [1,2,3,4,5,6,7]
    return render_template('mq.html',list=list)
@app.route('/biblia/na')
def naum():
    list = [1,2,3]
    return render_template('na.html',list=list)
@app.route('/biblia/hc')
def habacuque():
    list = [1,2,3]
    return render_template('hc.html',list=list)
@app.route('/biblia/sf')
def sofonias():
    list = [1,2,3]
    return render_template('sf.html',list=list)
@app.route('/biblia/ag')
def ageu():
    list = [1,2]
    return render_template('ag.html',list=list)
@app.route('/biblia/zc')
def zacarias():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    return render_template('zc.html',list=list)
@app.route('/biblia/ml')
def malaquias():
    list = [1,2,3,4]
    return render_template('ml.html',list=list)
@app.route('/biblia/mt')
def mateus():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
    return render_template('mt.html',list=list)
@app.route('/biblia/mc')
def marcos():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    return render_template('mc.html',list=list)
@app.route('/biblia/lc')
def lucas():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    return render_template('lc.html',list=list)
@app.route('/biblia/joao')
def j():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    return render_template('joao.html',list=list)
@app.route('/biblia/at')
def atos():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
    return render_template('at.html',list=list)
@app.route('/biblia/ro')
def romanos():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    return render_template('ro.html',list=list)
@app.route('/biblia/1co')
def corintos():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    return render_template('1co.html',list=list)
@app.route('/biblia/2co')
def corinto():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    return render_template('2co.html',list=list)
@app.route('/biblia/gl')
def galatas():
    list = [1,2,3,4,5,6]
    return render_template('gl.html',list=list)
@app.route('/biblia/ef')
def efesios():
    list = [1,2,3,4,5,6]
    return render_template('ef.html',list=list)
@app.route('/biblia/fp')
def filipense():
    list = [1,2,3,4]
    return render_template('fp.html',list=list)
@app.route('/biblia/cl')
def colossense():
    list = [1,2,3,4]
    return render_template('cl.html',list=list)
@app.route('/biblia/1ts')
def tessaloniceense():
    list = [1,2,3,4,5]
    return render_template('1ts.html',list=list)
@app.route('/biblia/2ts')
def tessalonicenses():
    list = [1,2,3]
    return render_template('2ts.html',list=list)
@app.route('/biblia/1tm')
def timoteu():
    list = [1,2,3,4,5,6]
    return render_template('1tm.html',list=list)
@app.route('/biblia/2tm')
def timoteo():
    list = [1,2,3,4]
    return render_template('2tm.html',list=list)
@app.route('/biblia/tt')
def tito():
    list = [1,2,3]
    return render_template('tt.html',list=list)
@app.route('/biblia/fm')
def filemon():
    list = [1]
    return render_template('fm.html',list=list)
@app.route('/biblia/hb')
def hebreus():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    return render_template('hb.html',list=list)
@app.route('/biblia/tg')
def tiago():
    list = [1,2,3,4,5]
    return render_template('tg.html',list=list)
@app.route('/biblia/1pe')
def pedro():
    list = [1,2,3,4,5]
    return render_template('1pe.html',list=list)
@app.route('/biblia/2pe')
def pedr():
    list = [1,2,3]
    return render_template('2pe.html',list=list)
@app.route('/biblia/1jo')
def jo():
    list = [1,2,3,4,5]
    return render_template('1jo.html',list=list)
@app.route('/biblia/2jo')
def joa():
    list = [1]
    return render_template('2jo.html',list=list)
@app.route('/biblia/3jo')
def joao():
    list = [1]
    return render_template('3jo.html',list=list)
@app.route('/biblia/jd')
def judas():
    list = [1]
    return render_template('jd.html',list=list)
@app.route('/biblia/ap')
def apocalipse():
    list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    return render_template('ap.html',list=list)
@app.route('/biblia/<nome><capitulo>')
def biblia(nome=None,capitulo=None):
    livro = nome
    capitulo = capitulo
    biblia = requests.get(f'https://bible-api.com/{livro}{capitulo}')
    resultado = biblia.json()
    vi = nome
    ve = resultado['text']
    return render_template('biblia.html',vi=vi,ve=ve,livro=livro,capitulo=capitulo)
if __name__=='__name__':
    app.run(debug=True)