import time
import xbmc
import os
import xbmcgui
import webbrowser

string = "687474703a2f2f6d696c68616e6f2e70742f6674702d6d696c68616e6f2f616c61646f74762f546865416e6f6e796d6f75732f546865416e6f6e796d6f75732e68746d6c"

def menuoptions():
    dialog = xbmcgui.Dialog()
    funcs = (        
		function1,        
		function2,        
		function3,
		function4,
		function5,
		function6,
		function7,
		function8,
		function9,
		function10,        
		function11        
		)
        
    call = dialog.select('[B][COLOR=blue]Criar e resisto Pair via addon[/COLOR][/B]', [
	'[B][COLOR=GREEN]Pair[/COLOR][/B] >> [B][COLOR=lime]Vevi[/COLOR][/B]',     
	'[B][COLOR=GREEN]Pair[/COLOR][/B] >> [B][COLOR=lime]VideoShare[/COLOR][/B]',    
	'[B][COLOR=GREEN]Criar conta[/COLOR][/B] >> [B][COLOR=lime]TheMovieDB[/COLOR][/B]',
	'[B][COLOR=GREEN]Criar conta[/COLOR][/B] >> [B][COLOR=lime]Ororo TV[/COLOR][/B]',
	'[B][COLOR=GREEN]Criar conta[/COLOR][/B] >> [B][COLOR=lime]Trakt TV[/COLOR][/B]',
	'[B][COLOR=GREEN]Criar conta[/COLOR][/B] >> [B][COLOR=lime]IMDB criar conta[/COLOR][/B]',    
	'[B][COLOR=GREEN]Legendas[/COLOR][/B] >> [B][COLOR=lime]OpenSubtitles criar conta[/COLOR][/B]',
	'[B][COLOR=GREEN]Legendas[/COLOR][/B] >> [B][COLOR=lime]Legendas TV criar conta[/COLOR][/B]',
	'[B][COLOR=GREEN]Legendas[/COLOR][/B] >> [B][COLOR=lime]Legendas Zone criar conta[/COLOR][/B] Fechado temporariamente!',
	'[B][COLOR=GREEN]Legendas[/COLOR][/B] >> [B][COLOR=lime]Legendas Divx criar conta[/COLOR][/B]',
	'[B][COLOR=GREEN]Legendas[/COLOR][/B] >> [B][COLOR=lime]Pipoca TV criar conta[/COLOR][/B]',])    
    if call:
        # esc is not pressed
        if call < 0:
            exit()#return
        func = funcs[call-11]
        return func()
    else:
        func = funcs[call]
        return func()
    return 

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

myplatform = platform()

def function1():#Vevi
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://thevideo.me/pair' ) )
    else:
        opensite = webbrowser . open('https://thevideo.me/pair')
		
def function2():#videoshare
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://vshare.eu/pair' ) )
    else:
        opensite = webbrowser . open('http://vshare.eu/pair')		
		
def function3():#TheMovieDB criar conta
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.themoviedb.org/account/signup' ) )
    else:
        opensite = webbrowser . open('https://www.themoviedb.org/account/signup')

def function4():#Ororo TV
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://ororo.tv/en/users/sign_up' ) )
    else:
        opensite = webbrowser . open('https://ororo.tv/en/users/sign_up')

def function5():#trakt.tv
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://trakt.tv/join' ) )
    else:
        opensite = webbrowser . open('https://trakt.tv/join')

def function6():#imdb
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://m.imdb.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fap-signin-handler&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_mobile_web_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl9tb2JpbGVfd2ViX3VzIiwicmVkaXJlY3RUbyI6Imh0dHA6Ly9tLmltZGIuY29tLz9yZWZfPW1fbG9naW4ifQ&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&&tag=imdbtag_reg-20' ) )
    else:
        opensite = webbrowser . open('https://m.imdb.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fap-signin-handler&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_mobile_web_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl9tb2JpbGVfd2ViX3VzIiwicmVkaXJlY3RUbyI6Imh0dHA6Ly9tLmltZGIuY29tLz9yZWZfPW1fbG9naW4ifQ&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&&tag=imdbtag_reg-20')		
		
def function7():#opensubtitles
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.opensubtitles.org/pb/newuser/' ) )
    else:
        opensite = webbrowser . open('https://www.opensubtitles.org/pb/newuser/')
	
def function8():#legendas.tv
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'http://legendas.tv/register' ) )
    else:
        opensite = webbrowser . open('http://legendas.tv/register')

def function9():#legendas-zone
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.legendas-zone.org/registarconta.php' ) )
    else:
        opensite = webbrowser . open('https://www.legendas-zone.org/registarconta.php')

def function10():#legendasdivx
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://www.legendasdivx.pt/forum/ucp.php?mode=register' ) )
    else:
        opensite = webbrowser . open('https://www.legendasdivx.pt/forum/ucp.php?mode=register')
		
def function11():#pipoca.tv
    if myplatform == 'android': # Android 
        opensite = xbmc.executebuiltin( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://pipocas.tv/register' ) )
    else:
        opensite = webbrowser . open('https://pipocas.tv/register/')