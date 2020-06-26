# Code to Initiate Web Server to Control Laptop from Phone

# Importing Libraries for Input


from pynput.keyboard import Key, Controller


# Dictionary of all Keyes
keys = {}
keys['space'] = Key.space
keys['up'] = Key.up
keys['down'] = Key.down
keys['left'] = Key.left
keys['right'] = Key.right

keys['alt'] = Key.alt
keys['alt_l'] = Key.alt_l
keys['alr_r'] = Key.alt_r
keys['backspace'] = Key.backspace
keys['caps_lock'] = Key.caps_lock
keys['cmd'] = Key.cmd
keys['cmd_l'] = Key.cmd_l
keys['cmd_r'] = Key.cmd_r
keys['ctrl'] = Key.ctrl
keys['ctrl_l'] = Key.ctrl_l
keys['ctrl_r'] = Key.ctrl_r
keys['delete'] = Key.delete
keys['end'] = Key.end
keys['enter'] = Key.enter
keys['esc'] = Key.esc

keys['f1'] = Key.f1
keys['f2'] = Key.f2
keys['f3'] = Key.f3
keys['f4'] = Key.f4
keys['f5'] = Key.f5
keys['f6'] = Key.f6
keys['f7'] = Key.f7
keys['f8'] = Key.f8
keys['f9'] = Key.f9
keys['f10'] = Key.f10
keys['f11'] = Key.f11
keys['f12'] = Key.f12

keys['home'] = Key.home
keys['insert'] = Key.insert
keys['num_lock'] = Key.num_lock
keys['page_down'] = Key.page_down
keys['page_up'] = Key.page_up
keys['prt_scr'] = Key.print_screen
keys['shift'] = Key.shift
keys['shift_l'] = Key.shift_l
keys['shift_r'] = Key.shift_r
keys['tab'] = Key.tab

keys['`'] = '`'
keys['1'] = '1'
keys['2'] = '2'
keys['3'] = '3'
keys['4'] = '4'
keys['5'] = '5'
keys['6'] = '6'
keys['7'] = '7'
keys['8'] = '8'
keys['9'] = '9'
keys['0'] = '0'
keys['-'] = '-'
keys['='] = '='
keys['/'] = '/'
keys['*'] = '*'
keys['['] = '['
keys[']'] = ']'
keys['\\'] = '\\'
keys[';'] = ';'
keys["'"] = "'"
keys[','] = ','
keys['.'] = '.'

keys['a'] = 'a'
keys['b'] = 'b'
keys['c'] = 'c'
keys['d'] = 'd'
keys['e'] = 'e'

keys['f'] = 'f'
keys['g'] = 'g'
keys['h'] = 'h'
keys['i'] = 'i'
keys['j'] = 'j'

keys['k'] = 'k'
keys['l'] = 'l'
keys['m'] = 'm'
keys['n'] = 'n'
keys['o'] = 'o'

keys['p'] = 'p'
keys['q'] = 'q'
keys['r'] = 'r'
keys['s'] = 's'
keys['t'] = 't'

keys['u'] = 'u'
keys['v'] = 'v'
keys['w'] = 'w'
keys['x'] = 'x'
keys['y'] = 'y'
keys['z'] = 'z'


# Media Keys
keys['play_pause'] = Key.media_play_pause
keys['next_song'] = Key.media_next
keys['prev_song'] = Key.media_previous
keys['volume_up'] = Key.media_volume_up
keys['volume_down'] = Key.media_volume_down
keys['mute'] = Key.media_volume_mute

keyboard = Controller()



# Code for Web App

from flask import Flask, render_template, url_for, redirect


remote = Flask(__name__)

@remote.route('/')
@remote.route('/index')
def index():
    return render_template('index.html')

@remote.route('/music')
def music():
    return render_template('music.html')


# Functions

# Music

# Plays/ Pauses music
@remote.route('/play_pause_music')
def play_pause_music():
    print('f6')
    keyboard.press(keys['play_pause'])
    keyboard.release(keys['play_pause'])
    return redirect(url_for('music'))
    # pass

# # Stops music
# @remote.route('/stop_music')
# def stop_music():
#     keyboard.press(keys['f6'])
#     keyboard.release(keys['f6'])
#     pass

# Increase Volume
@remote.route('/volume_up')
def volume_up():
    keyboard.press(keys['volume_up'])
    keyboard.release(keys['volume_up'])
    return redirect(url_for('music'))
    # pass

# Decrease Volume
@remote.route('/volume_down')
def volume_down():
    keyboard.press(keys['volume_down'])
    keyboard.release(keys['volume_down'])
    return redirect(url_for('music'))
  # pass

# Mute Volume
@remote.route('/mute')
def mute():
    keyboard.press(keys['mute'])
    keyboard.release(keys['mute'])
    return redirect(url_for('music'))
  # pass

# Previous Song
@remote.route('/prev_song')
def prev_song():
    keyboard.press(keys['prev_song'])
    keyboard.release(keys['prev_song'])
    return redirect(url_for('music'))
  # pass

# Next Song
@remote.route('/next_song')
def next_song():
    keyboard.press(keys['next_song'])
    keyboard.release(keys['next_song'])
    return redirect(url_for('music'))
  # pass


# Controller Type 1
@remote.route('/controller_1')
def controller_1():
    return render_template('controller_1.html')

@remote.route('/controller_1_left')
def controller_1_left():
    keyboard.press(keys['left'])
    keyboard.release(keys['left'])
    return redirect(url_for('controller_1'))

@remote.route('/controller_1_right')
def controller_1_right():
    keyboard.press(keys['right'])
    keyboard.release(keys['right'])
    return redirect(url_for('controller_1'))


# System Functions

# Importing System Functions

import os

# Shut Down Laptop
@remote.route('/shutdown')
def shut_down():
    os.system('shutdown /s /t 1')
    pass

# Restart Laptop
@remote.route('/restart')
def restart():
    os.system('shutdown /r /t 1')
    pass

# Sleep Laptop
@remote.route('/sleep')
def sleep():
    pass

# Lock Screen
@remote.route('/lock_screen')
def lock_screen():
    keyboard.press['cmd']
    keyboard.press['l']
    keyboard.release['cmd']
    keyboard.release['l']
    pass




# Self calling to run
if __name__ == '__main__':
    # remote.run(debug=True) # debug
    remote.run(host='192.168.1.100', port=5010) # Final run on server http://192.168.1.100:5010
