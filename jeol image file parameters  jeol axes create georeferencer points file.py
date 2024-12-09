import tkinter
import tkinter.filedialog
import pandas as pd
imagefileparameters=tkinter.filedialog.askopenfile()
df = pd.read_csv(imagefileparameters.name,sep=' ',header=None,names=range(13))
value = df[df=='$CM_MAG'].dropna(axis=0, how='all').dropna(axis=1, how='all')
magnification = df.loc[value.index.values[0],value.columns.values[0]+1]
value = df[df=='$CM_STAGE_POS'].dropna(axis=0, how='all').dropna(axis=1, how='all')
stagepositionx = df.loc[value.index.values[0],value.columns.values[0]+1]
stagepositiony = df.loc[value.index.values[0],value.columns.values[0]+2]
value = df[df=='$$SM_MICRON_BAR'].dropna(axis=0, how='all').dropna(axis=1, how='all')
ScaleBarPixelLength = df.loc[value.index.values[0],value.columns.values[0]+1]
value = df[df=='$$SM_MICRON_MARKER'].dropna(axis=0, how='all').dropna(axis=1, how='all')
ScaleBarMicronLength = df.loc[value.index.values[0],value.columns.values[0]+1]
ScaleBarMicronLength2 = ScaleBarMicronLength.split("um")[0]
MicronsPerPixel = float(ScaleBarMicronLength2)/float(ScaleBarPixelLength)
mmPerPixel = MicronsPerPixel/1000
value = df[df=='$CM_FULL_SIZE'].dropna(axis=0, how='all').dropna(axis=1, how='all')
PixelsX = df.loc[value.index.values[0],value.columns.values[0]+1]
PixelsY = df.loc[value.index.values[0],value.columns.values[0]+2]
#BLx=float(stagepositionx)-((float(PixelsX)/2)*mmPerPixel)
#BLy=float(stagepositiony)-((float(PixelsY)/2)*mmPerPixel)
#TRx=float(stagepositionx)+((float(PixelsX)/2)*mmPerPixel)
#BLy=float(stagepositiony)+((float(PixelsY)/2)*mmPerPixel)
TLx=float(stagepositionx)+((float(PixelsX)/2)*mmPerPixel)
TLy=float(stagepositiony)-((float(PixelsY)/2)*mmPerPixel)
TRx=float(stagepositionx)-((float(PixelsX)/2)*mmPerPixel)
TRy=float(stagepositiony)-((float(PixelsY)/2)*mmPerPixel)
BLx=float(stagepositionx)+((float(PixelsX)/2)*mmPerPixel)
BLy=float(stagepositiony)+((float(PixelsY)/2)*mmPerPixel)
BRy=float(stagepositiony)+((float(PixelsY)/2)*mmPerPixel)
BRx=float(stagepositionx)-((float(PixelsX)/2)*mmPerPixel)
f = open(imagefileparameters.name.split(".txt")[0]+".jpg.points", "w")
f.write("mapX,mapY,sourceX,sourceY,enable,dX,dY,residual")
f.write("\n")
line1=[str(BLx),str(BLy),"0",PixelsY,"1","0","0","0"]
f.write(','.join(line1))
f.write("\n")
line2=[str(TRx),str(TRy),PixelsX,"0","1","0","0","0"]
f.write(','.join(line2))
f.write("\n")
line3=[str(TLx),str(TLy),"0","0","1","0","0","0"]
f.write(','.join(line3))
f.write("\n")
line3=[str(BRx),str(BRy),PixelsX,PixelsY,"1","0","0","0"]
f.write(','.join(line3))
f.close()