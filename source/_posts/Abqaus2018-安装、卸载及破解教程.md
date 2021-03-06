---
title: Abqaus2018 安装、卸载及破解教程
mathjax: false
date: 2019-06-24 16:11:05
id: abqaus-install-uninstall
tags:
- 软件
- 学习
- 教程
categories:
- 实用教程
---

Abqaus2018 安装、卸载及破解教程

<!---more--->

## 安装及破解

0. Uninstall previous SSQ's "SIMULIA FlexNet Server" if one is installed


1. Install or update the SolidSQUAD Universal License Server for vendor DSSimulia

   If SolidSQUAD Universal License Server has never been installed
   on the computer:

     - unzip the "SolidSQUAD_License_Servers" folder from 
       "SSQ_UniversalLicenseServer_Core_<release-date>.zip" to any DRIVE ROOT 
       folder X:\ (like C:\, D:\, E:\ etc), so the path will be:

	X:\SolidSQUAD_License_Servers

     - unzip the "Vendors" folder from 
         "SSQ_UniversalLicenseServer_Module_DSSimulia_<release-date>.zip"
         to the "SolidSQUAD_License_Servers" folder

     - for Windows as administrator run "install_or_update.bat" from 
       "SolidSQUAD_License_Servers" folder and wait until it completes

     - for Linux as root run "install_or_update.sh" from 
       "SolidSQUAD_License_Servers" folder and wait until it completes

   -- OR --

   If SolidSQUAD Universal License Server is already installed, 
   but the release-date of "SSQ_UniversalLicenseServer_Core_<release-date>.zip"
   is newer than the installed one, update the server installation:

     - for Windows as administrator run "uninstall.bat" from 
       "SolidSQUAD_License_Servers" folder and wait until it completes

     - for Linux as root run "uninstall.sh" from 
       "SolidSQUAD_License_Servers" folder and wait until it completes

     - unzip the "SolidSQUAD_License_Servers" folder from 
       "SSQ_UniversalLicenseServer_Core_<release-date>.zip" to any DRIVE ROOT 
       folder X:\ (like C:\, D:\, E:\ etc), so the path will be:

	X:\SolidSQUAD_License_Servers

     - unzip the "Vendors" folder from 
         "SSQ_UniversalLicenseServer_Module_DSSimulia_<release-date>.zip"
         to the "SolidSQUAD_License_Servers" folder

     - for Windows as administrator run "install_or_update.bat" from 
       "SolidSQUAD_License_Servers" folder and wait until it completes

     - for Linux as root run "install_or_update.sh" from 
       "SolidSQUAD_License_Servers" folder and wait until it completes

   -- OR --

   If the release-date of "SSQ_UniversalLicenseServer_Core_<release-date>.zip" 
   is not newer than the installed one but the release-date of 
   "SSQ_UniversalLicenseServer_Module_DSSimulia_<release-date>.zip" is newer than the 
   installed one, update DSSimulia module only:

     - unzip the "Vendors" folder from 
         "SSQ_UniversalLicenseServer_Module_DSSimulia_<release-date>.zip"
         to the "SolidSQUAD_License_Servers" folder

     - for Windows as administrator run "install_or_update.bat" from 
       "SolidSQUAD_License_Servers" folder and wait until it completes

     - for Linux as root run "install_or_update.sh" from 
       "SolidSQUAD_License_Servers" folder and wait until it completes

2. Run setup of DS SIMILIA Suite 2018 (see SimuliaInstallationGuide.pdf for more info)

   For Win64 run DS.SIMULIA.SUITE.2018.WIN64.iso > 1 > setup.exe

   NOTE: To bypass FlexNET License server check on Windows, set the environment variable

     NOLICENSECHECK=true

   before starting the setupGUI.exe

   For Linux64 run DS.SIMULIA.SUITE.2018.LINUX64.iso > 1 > StartGUI.sh

   NOTE: To bypass the Linux distro checks, invoke StartGUI.sh with following exports:

     export DSYAuthOS_`lsb_release -si`=1
     export DSY_Force_OS=linux_a64
     export NOLICENSECHECK=true

   Select products to install

   "Abaqus Simulation Services V6R2018x" is mandatory to install!

   DO NOT install original "FLEXnet License server" from setup media!

3. In window "License Server configuration" select: "SIMULIA FLEXnet"
   In window for "SIMULIA FLEXnet License server" input for "License Server1": 27800@localhost

4. Finish setup

5. Install "SIMULIA Abaqus Associative Interfaces" (optional) for ProE, CATIA V5, SolidWorks
   from folder DS.SIMULIA.SUITE.2018.WIN64.iso > 2 > SIMULIA_Abaqus_AI

6. Enjoy!


Cracked by TeAM SolidSQUAD-SSQ

## 卸载

软媒魔方-》软件管理-》卸载软件，并进行“清理残留”

任务管理器-》停止“lmgrd”进程

手动删除文件夹
