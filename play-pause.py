import subprocess
def metadata(tipo):
    return runout(['/bin/playerctl', 'metadata','-f', tipo])
def notibody(): 
    '''Returns the body of the notification.'''
    tt = metadata('{{title}}')
    arti = metadata('{{artist}}')
    if len(tt) <= 1 and len(arti) <= 1:
        return 'No Playback Data'
    else:
        if len(arti) > 1 and len(tt) > 1:
            tt += ' - '
        tt += arti
        return tt
def runout(program):
    '''Returns the output of a command. courtesy of
       https://stackoverflow.com/questions/6657690/python-getoutput-equivalent-in-subprocess'''
    try:
        bout = subprocess.check_output(program, timeout=2)
        if len(bout) != 0:
            return bout.decode('UTF-8').rstrip()
        else:
            return False
    except subprocess.CalledProcessError as e:
        return False
def main():
    '''Sends a play or Pause command to a media player 
       and a system notification.'''
    runout(['/bin/playerctl', 'play-pause'])
    rs = metadata('{{status}}')
    if rs: # checks if a player is on.
        subprocess.run(['/bin/notify-send', '--expire-time=2500', '-i', metadata('{{playerName}}'), metadata('{{status}}'), notibody()])
    else:
        subprocess.run(['/bin/notify-send', '--expire-time=2500', 'Player not Found!'])
main()
