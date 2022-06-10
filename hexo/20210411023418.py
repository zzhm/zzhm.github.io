# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_14-01.49.31 163176
# Run by z on Sat Feb 27 16:49:21 2021
#
# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
# For test,update time：2021-03-26
import sys
import math
import os
from abaqus import *
from abaqusConstants import *
from caeModules import *
from odbAccess import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
Mdb()

#####################################################################################
#
# 参数定义，各段圆弧的首末端点均在一条直线上，初始圆弧与x轴相切（已经更新成任意）
# 单位制：SI-m-rad
#####################################################################################
radius = 0.030
theta  = math.pi/4

r1 = radius
r2 = radius
r3 = radius
r4 = radius


theta_1 = theta
theta_2 = theta
theta_3 = theta
theta_4 = theta

# 圆弧1, 参数方程的自变量范围 
arc_1_start = -0.5 * math.pi             
arc_1_end   = -0.5 * math.pi + theta_1

# 圆心
Xo1 = 0
Yo1 = r1

# 坐标
arc1_start_x  = Xo1  + r1 * cos(arc_1_start)
arc1_start_y  = Yo1  + r1 * sin(arc_1_start)
arc1_end_x    = Xo1  + r1 * cos(arc_1_end)
arc1_end_y    = Yo1  + r1 * sin(arc_1_end)



# 圆弧2, 参数方程的自变量范围 
arc_2_end   = arc_1_end + math.pi;
arc_2_start = arc_2_end - theta_2;

# 圆心
Xo2 = Xo1  + (r1 + r2)*sin(theta_1)
Yo2 = Yo1  - (r1 + r2)*cos(theta_1)

# 坐标，注意点的顺序，自变量的起点和圆弧的起点不一致
arc2_start_x  = Xo2  + r2 * cos(arc_2_end)
arc2_start_y  = Yo2  + r2 * sin(arc_2_end)
arc2_end_x    = Xo2  + r2 * cos(arc_2_start)
arc2_end_y    = Yo2  + r2 * sin(arc_2_start)

# 圆弧3, 参数方程的自变量范围 
arc_3_start   = arc_2_start - math.pi;
arc_3_end     = arc_3_start + theta_3;

# 圆心
Xo3 = Xo2  - (r3 + r2)*sin(theta_1- theta_2)
Yo3 = Yo2  + (r3 + r2)*cos(theta_1- theta_2)

# 坐标
arc3_start_x  = Xo3  + r3 * cos(arc_3_start)
arc3_start_y  = Yo3  + r3 * sin(arc_3_start)
arc3_end_x    = Xo3  + r3 * cos(arc_3_end)
arc3_end_y    = Yo3  + r3 * sin(arc_3_end)



# 圆弧4, 参数方程的自变量范围 
arc_4_end   = arc_3_end + math.pi
arc_4_start = arc_4_end - theta_4

# 圆心
Xo4 = Xo3 + (r3 + r4)*sin(theta_1 - theta_2 + theta_3)
Yo4 = Yo3 - (r3 + r4)*cos(theta_1 - theta_2 + theta_3)

# 坐标，注意点的顺序，自变量的起点和圆弧的起点不一致
arc4_start_x  = Xo4  + r4 * cos(arc_4_end)
arc4_start_y  = Yo4  + r4 * sin(arc_4_end)
arc4_end_x    = Xo4  + r4 * cos(arc_4_start)
arc4_end_y    = Yo4  + r4 * sin(arc_4_start)

# 圆环段2,厚度t,m
t   = 0.00025
# 末点角度
az  = math.atan(arc4_end_y/arc4_end_x)

# 输入位移沿着首末点连线，10mm
inputDisp = 0.010
# loadUx    = - math.cos(az)*inputDisp 
# loadUy    = - math.sin(az)*inputDisp
loadUx    = - math.cos(az)*inputDisp
loadUy    = - math.sin(az)*inputDisp

# 文件名和保存路径
curname   	= 'R' + str(int(radius*1000)) + 'Phi' + str(int(theta*180/math.pi))+ 'T025'
curpath   	= os.getcwd()
modelName 	= 'Model-' + curname
partName  	= 'Part-' + curname
partInst 	= partName + '-1'
stepName 	= 'Step-' + curname
jobName 	= 'Job-' + curname
xyplotName	= 'XYPlot-' + curname
viewpointName	= 'Viewport: ' + curname
dataName 		= curname + '.dat'
RF1         = 'RF1-' + curname
RF2         = 'RF2-' + curname
RFtotal     = 'RFtotal-' + curname
odbPath     = curpath + '\\Job-' + curname+'.odb'


###################################################################################
# Model
#
###################################################################################
mdb.Model(name=modelName, modelType=STANDARD_EXPLICIT)
s = mdb.models[modelName].ConstrainedSketch(name='curve_cons_solid', sheetSize=0.200)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)

# Skech
# 形状1
s.ArcByCenterEnds(center=(Xo1, Yo1), point1=(arc1_start_x, arc1_start_y), point2=(arc1_end_x, arc1_end_y), direction=COUNTERCLOCKWISE)
s.ArcByCenterEnds(center=(Xo2, Yo2), point1=(arc2_start_x, arc2_start_y), point2=(arc2_end_x, arc2_end_y), direction=CLOCKWISE)
s.ArcByCenterEnds(center=(Xo3, Yo3), point1=(arc3_start_x, arc3_start_y), point2=(arc3_end_x, arc3_end_y), direction=COUNTERCLOCKWISE)
s.ArcByCenterEnds(center=(Xo4, Yo4), point1=(arc4_start_x, arc4_start_y), point2=(arc4_end_x, arc4_end_y), direction=CLOCKWISE)


# 形状1偏置
s.offset(distance=t, objectList=(g[2], g[3], g[4],g[5]), side=LEFT)

# 连接首尾对应端点,见端点排序.png
s.Line(point1=(arc1_start_x, arc1_start_y), point2=(arc1_start_x, arc1_start_y + t))
s.Line(point1=(arc4_end_x, arc4_end_y), point2=s.vertices[13].coords)

# mdb.models[modelName].ConstrainedSketch(name='Sketch-' + curname,objectToCopy=s)

# 拉伸成实体
p = mdb.models[modelName].Part(name=partName, dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models[modelName].parts[partName]
p.BaseSolidExtrude(sketch=s, depth=0.010)
s.unsetPrimaryObject()
p = mdb.models[modelName].parts[partName]
# del mdb.models[modelName].sketches['curve_cons_solid']

# 分割
p = mdb.models[modelName].parts[partName]
c = p.cells
# pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
pickedCells =c.findAt(((arc1_start_x, arc1_start_y + 0.5*t, 0.005),))
v, e, d = p.vertices, p.edges, p.datums
p.PartitionCellByPlaneThreePoints(point1=v[16], point2=v[1], point3=v[2],cells=pickedCells)

p = mdb.models[modelName].parts[partName]
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#2 ]', ), )
v1, e1, d1 = p.vertices, p.edges, p.datums
p.PartitionCellByPlaneThreePoints(point1=v1[4], point2=v1[9], point3=v1[13], cells=pickedCells)

p = mdb.models[modelName].parts[partName]
c = p.cells
pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
v, e, d = p.vertices, p.edges, p.datums
p.PartitionCellByPlaneThreePoints(point1=v[6], point2=v[9], point3=v[15], cells=pickedCells)

######################################################################################
# 材料，截面
#
######################################################################################
mdb.models[modelName].Material(name='Material-1')
mdb.models[modelName].materials['Material-1'].Elastic(table=((2408000000.0, 0.407), ))

mdb.models[modelName].HomogeneousSolidSection(name='Section-1', material='Material-1', thickness=None)

p = mdb.models[modelName].parts[partName]
c = p.cells
cells = c.getSequenceFromMask(mask=('[#f ]', ), )
region = regionToolset.Region(cells=cells)
p = mdb.models[modelName].parts[partName]
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', thicknessAssignment=FROM_SECTION)

####################################################################################
# 装配	
#
####################################################################################
a = mdb.models[modelName].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models[modelName].parts[partName]
a.Instance(name=partInst, part=p, dependent=ON)

# 参考点
a = mdb.models[modelName].rootAssembly
a.ReferencePoint(point=(arc4_end_x, arc4_end_y + 0.5*t, 0.005))	
r1 = a.referencePoints
refPoints1=(r1[4], )
a.Set(referencePoints=refPoints1, name='Set-refpoint')

####################################################################################
# 分析	
#
####################################################################################
mdb.models[modelName].StaticStep(name=stepName, previous='Initial', nlgeom=ON)
mdb.models[modelName].fieldOutputRequests['F-Output-1'].setValues(variables=('E', 'S', 'U'),timeInterval=0.05)

regionDef=mdb.models[modelName].rootAssembly.sets['Set-refpoint']
# timeInterval=0.05 设置输出的步数
mdb.models[modelName].historyOutputRequests['H-Output-1'].setValues(variables=(
    'RF1', 'RF2', 'RF3', 'RM1', 'RM2', 'RM3', 'TF1', 'TF2', 'TF3', 'TM1', 
    'TM2', 'TM3'), timeInterval=0.05, region=regionDef, sectionPoints=DEFAULT, rebar=EXCLUDE)

# 耦合	
a           = mdb.models[modelName].rootAssembly
r1          = a.referencePoints
refPoints1  = (r1[4], )
region1     = a.Set(referencePoints=refPoints1, name='m_Set-RP1')
s1          = a.instances[partInst].faces
#side1Faces1 = s1.getSequenceFromMask(mask=('[#10 ]', ), )
side1Faces1 = s1.findAt(((arc4_end_x, arc4_end_y + 0.5*t, 0.005),))

region2=a.Surface(side1Faces=side1Faces1, name='s_Surf-end')
mdb.models[modelName].Coupling(name='Constraint-1', controlPoint=region1, 
    surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC, 
    localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)

# Load 负载，固定约束
a      = mdb.models[modelName].rootAssembly
f1     = a.instances[partInst].faces
#faces1 = f1.getSequenceFromMask(mask=('[#200 ]', ), )
faces1 = f1.findAt(((arc1_start_x, arc1_start_y + 0.5*t, 0.005),))
region = regionToolset.Region(faces=faces1)
mdb.models[modelName].EncastreBC(name='BC-fix', createStepName=stepName, region=region, localCsys=None)

##################################################################################################
# 边界，输入位移，其余的自由度也要约束，不然提醒 Too many attempts made for this increment。
#
##################################################################################################
a = mdb.models[modelName].rootAssembly
region = a.sets['Set-refpoint']
mdb.models[modelName].DisplacementBC(name='BC-displacement', createStepName=stepName, 
	region=region, u1=loadUx, u2=loadUy, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0, 
    amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='', localCsys=None)
	
####################################################################################
# Mesh 网格,ansys里的用的是0.5mm，这里用1mm与ansys的结果相同
# C3D20R与C3D8R存在问题，网格太大/小数据均不准，
####################################################################################

# elemType1 = mesh.ElemType(elemCode=C3D20R, elemLibrary=STANDARD)
# elemType2 = mesh.ElemType(elemCode=C3D15,  elemLibrary=STANDARD)
# elemType3 = mesh.ElemType(elemCode=C3D10,  elemLibrary=STANDARD)
# C3D8R
# elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD, kinematicSplit=AVERAGE_STRAIN, 
#	secondOrderAccuracy=OFF, hourglassControl=DEFAULT, distortionControl=DEFAULT)
# elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
# elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)

# C3D20RH is better,
# elemTypes: A sequence of ElemType objects, one for each element shape applicable to the regions.
elemType1 = mesh.ElemType(elemCode=C3D20RH, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D15H, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D10M, elemLibrary=STANDARD, secondOrderAccuracy=OFF, distortionControl=DEFAULT)

p = mdb.models[modelName].parts[partName]
#cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
pickedRegions =(p.cells, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2, elemType3))

p = mdb.models[modelName].parts[partName]
p.seedPart(size=0.0005, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models[modelName].parts[partName]
p.generateMesh()

####################################################################################
# Job
# 
####################################################################################
mdb.Job(name=jobName, model=modelName, description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=2,numDomains=2, numGPUs=0)
	
mdb.jobs[jobName].submit(consistencyChecking=OFF)

# Wait for completion
mdb.jobs[jobName].waitForCompletion()

# Save model
mdb.saveAs(pathName=curpath+'\\'+curname+'.cae')

##################################################################################################
# 后处理
#
##################################################################################################
from odbAccess import *
odb   = openOdb(path=odbPath)
stepF = odb.steps[stepName]
# print stepF.historyRegions.keys()
region  = stepF.historyRegions['Node ASSEMBLY.1']
rf1data = region.historyOutputs['RF1'].data
rf2data = region.historyOutputs['RF2'].data

# rftotal=rf1data*math.cos(phi1/2)+rf2data*math.sin(phi1/2)
 
import numpy as np
rf1x = [x[0] for x in rf1data]
rf1y = [x[1] for x in rf1data]
rf2y = [x[1] for x in rf2data]

ft     = np.array(rf1y)*math.cos(az)+np.array(rf2y) *math.sin(az)
rtotal = zip(rf1x,list(ft))

# 搜索最大Mises应力
stressHistory = []   #存储每一步的应力值
maxValue = None
stressOutputExists = FALSE
for step in odb.steps.values():
	for frame in step.frames:
		try: 
			stress = frame.fieldOutputs['S']
			stressOutputExists = TRUE
		except KeyError:    # 跳过不包含应力输出的帧
			continue
		for stressValue in stress.values:
			if (not maxValue or
					stressValue.mises > maxValue.mises):
					maxValue = stressValue
					maxStep, maxFrame = step, frame  
		stressHistory.append(maxValue.mises/1000000.0)  # MPa
                    
# append会修改a本身，并且返回None。不能把返回值再赋值给a,即不能 a=a.append(b)            
# 如果odb文件中没有输出应力结果，则抛出异常。
if not stressOutputExists:
    raise Exception("No Stress Output in Odb file")
    
####################################################################################
# 保存数据，使用xlwt
#
####################################################################################

import xlwt

# 创建工作簿
workbook   = xlwt.Workbook(encoding='utf-8')  
# 创建sheet
data_sheet = workbook.add_sheet(curname)  

row0 = ['Displacement',RF1, RF2, RFtotal, 'maxStress']
row1 = ['Max Mises Stress','Step','Frame','Part Instance','Element Label','Section Point','Integration Point']
row2 = [maxValue.mises/1000000.0, maxStep.name, maxFrame.frameId, maxValue.instance.name, maxValue.elementLabel, maxValue.sectionPoint, maxValue.integrationPoint]

# 保存位移-反力数据
# 生成表头,xlwt中是行和列都是从0开始计算的
for i in range(len(row0)):
	data_sheet.write(0, i, row0[i])

# 写入数据，按照列写入
for i in range(len(np.array(rf1x))):
	data_sheet.write(i+1, 0, np.array(rf1x)[i]*inputDisp)  
	data_sheet.write(i+1, 1, np.array(rf1y)[i])
	data_sheet.write(i+1, 2, np.array(rf2y)[i])
	data_sheet.write(i+1, 3, ft[i])
	data_sheet.write(i+1, 4, stressHistory[i])   
	
	
# 保存应力信息
for i in range(len(row1)):
	data_sheet.write(i+1, len(row0)+2, row1[i])  
	data_sheet.write(i+1, len(row0)+3, row2[i])  
	
#保存文件
workbook.save(curname + '.xls')	

# 保存数据，使用pandas
# import pandas as pd
# import numpy as np
# data={"Displacement":np.array(rf1x),RF1:np.array(rf1y),RF2:np.array(rf2y),RFtotal:ft}
# df=pd.DataFrame(data,index=range(11))

# #将DataFrame存储为csv,index表示是否显示行名，default=True
# df.to_csv(curname+'.csv',index=False, sep=',')


# 保存，直接操作文件
# data = rf1data + rf2data + tuple(rtotal)
# simdata = open(dataName,'w')
# for aa,bb in data:
    # simdata.write('%f  %f \n'%(aa,bb))	
# simdata.close()

# 输出最大Mises应力的详细信息
#print("Max Mises Stress %E in:" %maxValue.mises)
#print("Step:             ", maxStep.name) 
#print("Frame:            ", maxFrame.frameId)   
#print("Part Instance:    ", maxValue.instance.name)
#print("Element Label:    ", maxValue.elementLabel)
#print("Section Point:    ", maxValue.sectionPoint)
#print("Integration Point:", maxValue.integrationPoint)

##################################################################################################
# 作图
#
##################################################################################################
import numpy as np 
from matplotlib import pyplot as plt 

plt.subplot(2,1,1)
plt.plot(np.array(rf1x)*inputDisp*1000, np.array(rf1y), color="blue",  linewidth=2, linestyle="-", marker='s', label=RF1)
plt.plot(np.array(rf1x)*inputDisp*1000, np.array(rf2y), color="green", linewidth=2, linestyle="-", marker='.', label=RF2)
plt.plot(np.array(rf1x)*inputDisp*1000, ft,             color="red",   linewidth=2, linestyle="-", marker='o', label=RFtotal)
plt.legend(loc='upper right') 
plt.title("Displacement-Force-" + curname) 
plt.xlabel("Displacement /mm") 
plt.ylabel("Force /N") 

plt.subplot(2,1,2)
plt.plot(np.array(rf1x)*inputDisp*1000, np.array(stressHistory), color="blue", linewidth=2, linestyle="-", marker='o')
plt.title("Displacement-Stress-" + curname) 
plt.xlabel("Displacement /mm") 
plt.ylabel("Stress /MPa") 

# 保存图片
plt.tight_layout() 
plt.savefig(curpath+'\\'+curname+'.png', dpi=300,bbox_inches = 'tight')
#plt.show()
plt.close()



