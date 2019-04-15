from pytube import YouTube
#import moviepy as mp
from moviepy.editor import VideoFileClip, concatenate_videoclips
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

def download(link="https://www.youtube.com/watch?v=xWOoBJUqlbI"):
    SAVE_PATH = "E:/Videos"
    yt = YouTube(link) 
    d_video = yt.streams.first() 
    #d_video.download(SAVE_PATH)#filename = SAVE_PATH+'/vid.mp4') 
    d_video.download(SAVE_PATH,filename='vid')
    #print(d_video.default_filename)
    #os.rename(yt.streams.first().default_filename, 'new_filename.ext')
    print('Task Completed!') 

class VideoEditer():
    def __init__(self,filepath="E:/Videos",tolerance=30,step=0.5):
        self.video = VideoFileClip(filepath+"/vid.mp4")
        self.tolerance = tolerance
        self.debug_plot = False
        self.debug_txt = False
        self.filepath = filepath
        self.step = step
        pass

    def download(self):
        pass

    def extract_audio(self):
        self.audio = self.video.audio
        self.audio.write_audiofile(self.filepath+"/aud.wav")
        pass

    def run(self):
        self.find_nulls()
        e = self.cut_video()
        if not e:
            return self.save_result()
        return e 

    def find_nulls(self):
        rate,data = wavfile.read(self.filepath+"/aud.wav")
        if self.debug_txt:
            print("\n\n",rate,"\n")
        data_l,data_r = data.transpose()
        step = int(self.step*rate)
        drop = len(data_l)%step
        if drop:
            bin_data = np.delete(data_l,np.s_[(-1*drop):])
        if self.debug_txt:
            print("length of data ::",len(data_l),"\n")
            print("Number of bins ::",len(data_l)/step,"\n")
            print("Number of droped points at end",drop,"\n")
            print("Time of data in seconds ::",len(bin_data)/rate,"\n")
        bin_data = np.abs(bin_data)
        bin_data = np.array(np.split(bin_data,int(len(bin_data)/step)))
        if self.debug_txt:
            print("Actual number of bins ::",len(bin_data),'\n')
        avg_ampl = np.mean(bin_data,axis=1)
        if self.debug_plot:
            plt.plot(avg_ampl)
            plt.show()
        tol = self.tolerance
        index = np.where(avg_ampl<tol)[0]
        if self.debug_txt:
            print(len(avg_ampl),"\n")
            print(len(index),'\n')
        if self.debug_plot:
            plt.plot(avg_ampl)
        nulls = np.full(len(index),30)
        if self.debug_txt:
            print(len(nulls),'\n')
        maxa = avg_ampl.max()
        start = index[0]*step/rate
        s_index = index[0]
        ss_time = []
        ss_indx = []
        for i,j in zip(index[:-1],index[1:]):
            if j-i == 1:
                pass
            else:
                ss_time.append([start,i*step/rate])
                start = j*step/rate
                ss_indx.append([s_index,i])
                s_index = j
        if not s_index == i:
            
            ss_time.append([start,i*step/rate])
            ss_indx.append([s_index,i])
            #if not s_index-1 == i:
            #    ss_time.append([(s_index-1)*step/rate,i*step/rate])
            #    ss_indx.append([s_index-1,i])
        if self.debug_plot:
            for i,j in ss_indx:
                plt.axvspan(i,j,ymax=maxa,color='r',alpha=0.5)
            print(ss_time,'\n')
            print(ss_indx,'\n')
            plt.show()
        if self.debug_plot:
            plt.plot(data_l)
            for i,j in ss_indx:
                plt.axvspan(i*step,j*step,ymax=maxa,color='r',alpha=0.5)
            plt.show()
        self.time_slices = ss_time

    def cut_video(self):
        nullClips = []
        length = 0
        for start,finish in self.time_slices:
            if finish > self.video.duration:
                finish = self.video.duration-0.01
            #length += finish-start
            nullClips.append(self.video.subclip(start,finish))
        print(len(nullClips))
        if len(nullClips):
            try:
                self.final_clip = concatenate_videoclips(nullClips)
            except:
                print("Got that exception")
                print(nullClips[-1].duration)
                self.final_clip = concatenate_videoclips(nullClips[:-1])
        else:
                return "No Clips Meet those requirements"
    
        length = self.final_clip.duration
        if length > 60:
                return "Final Clip Too Long "

        return False
    
    def save_result(self):
        self.final_clip.write_videofile(self.filepath+"/nullVid.mp4")
        return self.filepath+'/nullVid.mp4'
        pass

if __name__ == "__main__":
    pass