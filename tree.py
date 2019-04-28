from PIL import Image,ImageDraw
import sys
import numpy as np


def generate_line_paths(starts,amount,weight,volitility):
    for point in starts:
        for i in range(amount):
            pass




class Tree():
    class Branch():
        def __init__(self,start,length,angle,weight,color):
            self.start = [start[0],start[1]]
            self.length = length
            self.angle = angle

            
            if weight < 1:
                self.weight = 1
            else:              
                self.weight = weight
            self.color = color

        def gen_vector(self,symetry):
            self.sym = np.random.rand()*symetry
            self.angle += self.sym*np.abs(self.angle)
            self.top = [
                self.length*np.sin(self.angle/180*np.pi)+self.start[0],
                -self.length*np.cos(self.angle/180*np.pi)+self.start[1]
            ]
            
           

        def make(self,draw,typ='line'):
            if typ == 'line':
                draw.line((tuple(self.start),tuple(self.top)),fill=self.color,width=int(self.weight*1))

            return True

    def __init__(self,
            sangle=90,
            length=400,
            width=35,
            angle=90,
            branch_number=4,
            itterations=6,
            initial_branch=1,
            R=255,
            G=255,
            B=255,
            BR=0,
            BG=0,
            BB=0,
            image_size_x = 2000,
            image_size_y = 2000,
            w_factor=0.7,
            l_factor=0.9,
            l_vol=0.5,
            b_vol=0,
            a_vol=0.2,
            symetry = 0,
            typ='line'
            ):
        color = (R,G,B)
        back_color=(BR,BG,BB)
        image_size = [image_size_x,image_size_y]
        self.im = Image.new(mode='RGB',size=image_size,color=back_color)
        self.draw = ImageDraw.Draw(self.im)

        self.start_args = [[width],[length],[sangle]]

        self.image_size = image_size
        self.w_factor = w_factor
        self.l_factor = l_factor
        self.branch_number = branch_number
        self.angle = angle
        self.l_vol = l_vol
        self.b_vol = b_vol
        self.a_vol = a_vol
        self.itterations = itterations
        self.typ = typ
        self.initial = True
        self.color = color
        self.initial_branch = initial_branch
        self.symetry = symetry
        self.start = [self.image_size[0]/2,self.image_size[1]]

    def makeBranches(self,starts,weights,lengths,angles,itteration=0):
        print()
        print(starts[0])
        #print(weights)
        #print(lengths)
        
        new_starts = []
        new_weights = []
        new_lengths = []
        new_angles = []
        for start,weight,angle,length in zip(starts,weights,angles,lengths):
            branch_number = self.branch_number + np.random.randint(0,self.b_vol+1)
            if self.initial:
                branch_number = self.initial_branch
                
            for b in range(branch_number):
                cl_vol = (1-np.random.rand()*self.l_vol)
                ca_vol = self.a_vol/2 - np.random.rand()*self.a_vol
                b_length = length * cl_vol
                if branch_number > 1 and not self.initial:
                    b_angle = angle - self.angle/2 + b*self.angle/(branch_number-1)
                    b_angle += ca_vol*b_angle
                elif branch_number > 1 and self.initial:
                    b_angle =  b*self.angle/(branch_number-1) - self.angle/2
                    print(b_angle)
                else:
                    b_angle = 0
                #print(b_angle)
                b_weight = weight * cl_vol
                branch = self.Branch(start,b_length,b_angle,b_weight,self.color)
                branch.gen_vector(self.symetry)
                if branch.make(self.draw,self.typ):
                    new_starts.append(branch.top)
                    new_lengths.append(branch.length*self.l_factor)
                    new_weights.append(branch.weight*self.w_factor)
                    new_angles.append(branch.angle)
                
        if itteration <= self.itterations:
            self.initial = False
            itteration += 1
            self.makeBranches(new_starts,new_weights,new_lengths,new_angles,itteration)
        else:
            self.im.save("E:/Trees/tree.png",'PNG')
            return True
            
if __name__ == '__main__':
    tree = Tree(image_size=[2000,2000] ,initial_branch = 1,branch_number=4,symetry=0.0,angle=90,
    itterations=6,a_vol=0.2,l_vol=0.5,b_vol=0,w_factor=0.7,l_factor=0.9)#,b_vol=4)
    tree.makeBranches([tree.start],[35],[400],[70])