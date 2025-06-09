import random
from screeninfo import get_monitors
from psychopy import visual, event, data, core, logging
import psychopy.iohub as io
from psychopy.hardware import keyboard
from psychopy import prefs, gui
import numpy as np
import os
from numpy.random import randint
from pylsl import StreamInfo, StreamOutlet
from psychopy import logging
from psychopy.hardware import brainproducts
from datetime import date


# 파일 저장
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

psychopyVersion = '2024.2.4'
expName = 'face-word_stroop'
expInfo = {
    'participant' : f"{randint(0, 999999):06.0f}",
    'session' : '001'
}  
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit() 
expInfo['date'] = date.today().strftime('%Y%m%d')
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath= os.path.abspath(__file__),
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

frameTolerance = 0.001 # how close to onset before 'same' frame

# # rcs
# logging.console.setLevel(logging.DEBUG)
# rcs = brainproducts.RemoteControlServer(host='192.168.137.219', port=6700)

# # 파일 경로 설정
# base_dir = r"C:/Vision/Workfiles"
# file_name = f"{expInfo['participant']}_{expName}_{expInfo['date']}.rwksp"
# # eeg workspace
# workspace_path = os.path.join(base_dir, '')

'''
eeg workspace는 brain product 소프트웨어에서 채널을 설정한 파일 주소로 지정해주시면 됩니다.
task는 스페이스바를 누를 시 시작되며, 무작위 이미지 1초, fixation 1~5초 무작위 로 구현하였고 총 106장의 이미지를 보여준 후에 종료됩니다.
이미지에 대한 응답은 오른쪽 마우스/왼쪽 마우스로 받습니다.
중간에 esc 키를 눌러서 종료할 수 있습니다.
주석은 rcs(eeg), lsl(fNRIS) 마커를 보내는 코드들입니다. 
이전 코드를 참고하여 적었으나, 혹시 안될 수 있으니 확인 부탁드립니다.

ps. 오늘도 ~!~!~!~!화이팅 !~!~!~!~!

'''

# # RCS open 호출
# rcs.open(expName,
#          workspace=workspace_path,
#          participant=expInfo['participant'])

         
# # LSL 스트림 생성 (Aurora에서 설정한 Trigger in 이름과 동일해야 함)
# info = StreamInfo(name='stroop_task', type='Markers', channel_count=1, channel_format='int32', source_id='Example') # sets variables for object info

# outlet = StreamOutlet(info) # initialize stream.



for monitor in get_monitors():
    width = monitor.width
    height = monitor.height
    
prefs.general['winType'] = 'pyglet'

event.globalKeys.clear() # global event key 초기화

base_folder = 'stimuli-ha-sa'
happy_folder = os.path.join(base_folder, 'incong-cong-HA')
sad_folder = os.path.join(base_folder, 'incong-cong-SA')

# 이미지 파일 읽기
happy_files = [os.path.join(happy_folder, f) for f in os.listdir(happy_folder) if f.lower().endswith(('.png'))]
sad_files = [os.path.join(sad_folder, f) for f in os.listdir(sad_folder) if f.lower().endswith(('.png'))]

# 합쳐서 무작위 순서로 섞기
all_images = happy_files + sad_files
random.shuffle(all_images)

# win 초기화
win = visual.Window(color='black', fullscr=True, units='pix')
win_width, win_height = win.size

# 원본 이미지 크기 (예: 1719 x 1719)
original_width = 1719
original_height = 1719
original_ratio = original_width / original_height  # 여기선 1.0

# 기준 비율 설정 (창의 70%)
scale_ratio = 0.7
max_width = win_width * scale_ratio
max_height = win_height * scale_ratio

# 윈도우 비율에 맞게 조정 (비율 유지)
if original_ratio >= 1:  # 가로가 더 크거나 정사각형
    target_width = min(max_width, max_height * original_ratio)
    target_height = target_width / original_ratio
else:  # 세로가 더 긴 경우
    target_height = min(max_height, max_width / original_ratio)
    target_width = target_height * original_ratio

stim = visual.ImageStim(win=win, size=(target_width, target_height), pos=(0, 0))

# message
start_message = visual.TextStim(win, font='Malgun Gothic', color='white', text='START', height=70)
fixation_message = visual.TextStim(win, font='Malgun Gothic', color='white', text='+', height=70)
response_message = visual.TextStim(win, font='Malgun Gothic', color='white', text='마우스로 응답해주세요', height=70)
finish_message = visual.TextStim(win, font='Malgun Gothic', color='white', text='END', height=70)
running = True

clock = core.Clock()

# esc 버튼으로 바로 종료
def escape():
    win.close()
    core.quit()
event.globalKeys.add(key='escape', func=escape)

mouse = event.Mouse()

#start
start_message.draw()
win.flip() 

key = event.waitKeys(keyList=['space'])

if 'space' in key:
    # rcs.sendAnnotation('start', 'START')
    # outlet.push_sample(x=[10])
    print('start')



# rcs.openRecorder()
# rcs.mode = 'monitor'
# rcs.startRecording()


trial_number = 0

'''
    *lsl 마커
    1 : left(congruent)
    2 : right(incongruent)
    10 : start
    30 : stimuli
    50 : fixation
    100 : end
'''

while running:

    if trial_number < 107 :

        # 이미지 제시
        img = all_images[trial_number]
        stim.image = img
        stim.draw()
        win.flip()
        # rcs.sendAnnotation('Stimuli', 'STIM')
        # outlet.push_sample(x=[30])
        trial_number+=1
        core.wait(1.0)  # 1초간 제시

        response_message.draw()
        win.flip()
        # 최대 5초 동안 대기하면서 마우스 클릭 감지
        timer = core.Clock()
        clicked_button = None  # 어떤 버튼이 눌렸는지 저장

        while timer.getTime() < 5.0:
            buttons = mouse.getPressed()
            if buttons[0]:  # 왼쪽 클릭
                # rcs.sendAnnotation('left', 'RES')
                # outlet.push_sample(x=[1])
                break
            elif buttons[2]:  # 오른쪽 클릭
                # rcs.sendAnnotation('right', 'RES')
                # outlet.push_sample(x=[2])
                break
            core.wait(0.01)
        
        fixation_message.draw()
        win.flip()
        # rcs.sendAnnotation('fixation', 'FIX')
        # outlet.push_sample(x=[50])
        # 긴장을 유도하기 위해 fixation time을 3s~5s로 랜덤하게 구현현
        fixation_time = np.random.randint(3000, 5001)
        core.wait(fixation_time*0.001)


    #   종료--------------------------------------------------------------------------
    if trial_number == 107:
        print('finish')
        # rcs.sendAnnotation('finish', 'END')
        # outlet.push_sample(x=[100])
        finish_message.draw()
        win.flip()
        core.wait(10)
        # rcs.mode = 'default'
        running = False

# 종료
win.close()
core.quit()