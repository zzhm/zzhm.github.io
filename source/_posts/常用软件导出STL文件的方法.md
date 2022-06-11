---
title: 如何导出STL文件
id: how-to-prepare-stl-files
date: 2021-04-20 14:20:11
tags:
- stl
- 软件教程
categories:
- 实用教程
---



STL is the standard file type used by most additive manufacturing systems. STL is a triangulated representation of a 3D CAD model (Figure 1).

STL is the standard file type used by most additive manufacturing systems.

STL is a triangulated representation of a 3D CAD model (Figure 1).

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20210420154956.jpg)

The triangulation (or poly count) of a surface will cause faceting of the 3D model. The parameters used for outputting a STL will affect how much faceting occurs (Figures 2 and 3). You cannot build the model smoother than the STL file. If the STL is coarse and faceted the physical 3D printed model will be coarse and faceted as well. However, the smoother/ less faceted your surface is, (the higher the poly count or triangulation) the larger your file. 3D printing can only accept a certain file size; therefore it’s important to find a balance between your model, its desired surface, and the 3D printing process of your choice.

![](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20210420155002.png)

When exporting to STL in your CAD package, you may see parameters for chord height, deviation, angle tolerance, poly count, or something similar. These are the parameters that affect the faceting of the STL. We’ve compiled tips on exporting for the best “surface: file” size ratio below.

## Preparing your files

The following step-by-step instructions for converting CAD files to STL came from each CAD software company’s website or from 3D printing and design user forums; it’s an overall simplified step-by-step process from the greater 3D printing community. If your CAD software is not listed below or if you require additional assistance, please contact your CAD software technical support for information about exporting to an STL.

## Select your CAD software:

**3D Modeling for Beginners**

- [Tinkercad](#Tinkercad )
- [SketchUp](#SketchUp)

**3D Modeling for Engineers**

- [Autodesk Inventor](#autodesk)
- [CATIA](#catia)
- [IronCAD](#ironCAD)
- [Rhinoceros](#rhinoceros)
- [PTC Creo Parametric](#PTC Creo)
- [Solid Edge](#solidedge)
- [SolidWorks](#solidworks)
- [NX](#NX (Formerly UGS NX))

**3D Modeling for Artists**

- [Blender](#blender)
- [ZBrush](#ZBrush)
- [Maya](#maya)

*Don't have CAD software? SolidView is an affordable solution for non-CAD users to prepare STL files from many popular CAD formats. [Start your free trial today](http://www.solidview.com/Products).*

## Tinkercad

Tinkercad is great for 3D printing simple geometrical objects. Its interface was created with 3D printing in mind.

1. Design -> Download for 3D Printing -> .STL

## SketchUp

SketchUp does not offer STL creation directly within the program. Download the extension for .STL [here](https://extensions.sketchup.com/en/content/sketchup-stl) (note: this plugin is open-source and updated frequently).

1. Download and install the plugin
2. Select Tools -> Export to DXF or STL and select the units for your model (millimeters is recommended)

Tip: SketchUp isn’t inherently built for model production therefore it’s useful to check your SketchUp file for additional feature accuracies once it’s exported from the interface. We recommend uploading your SketchUp file into [Meshmixer](http://www.meshmixer.com/) (a free program from Autodesk) to check your file for faceting and fix any surface flaws.

Note: We don’t recommend Sketchup for use with 3D printing as it does not export well and is best for early design sketches rather than producing physical models.

## Autodesk Inventor

1. Select IPro --> Print --> 3D Print Preview
2. Select Options and choose desired resolution and click OK
3. Within the preview window, select Save Copy As or Send to 3D Print Service
4. Save As type to STL File (`*.stl`)

![stl](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20210420155007.jpg)

Note: The “High” setting will also produce the largest file size. From Low, Medium to High, the hairdryer sample file in Inventor went from about 6.7MB to 17.6MB to 50MB.

![stl](https://raw.githubusercontent.com/zzhm/zzhm.github.io/images/hexo/20210420155010.jpg)

Tip: Before finalizing your export, select the Options tab. Within this window, you can select the resolution (faceting) for your model (High, Medium, Low and Custom) and check that your units are correct. The “High” setting will produce a large file size. Autodesk Inventor allows you to save both individual parts and assemblies in STL format, at all design levels. For a quick overview of designing in Inventor, click [here](https://www.youtube.com/watch?v=akem4NYbFCY).
To check your modifiers have been applied before exporting:

1. Tools -> Rebuild All (this ensures that the design data contains recent changes, and that it is not corrupt)
2. File -> Save Copy As -> STL (.stl)
3. Select High and click OK

Note: To change the values associated with each of the resolution settings (High/Medium/Low) you need to edit the Windows registry.

## CATIA

1. Select STL command (we recommend setting maximum segmentation to 0.015 mm)
2. Select the model -> Yes -> Export

Note: CATIA V5 is capable of creating STL files from CATPart files, but not from assemblies (CATProduct files) or geometrical representations (car files). Therefore, source files, including those saved in a neutral format (i.e. STEP or IGES), must be saved as CATParts. If the source design was saved as an assembly, it is imported to CATIA as a CATProduct. To create an STL file from it, you must first convert it to a multi-bodied part. The procedure described below is one of several methods for doing this.
Saving CATProduct files as CATPart Files for 3D printing:

1. File Menu -> Open -> select your source file (assemblies import as CATProduct)
2. Save the imported CATProduct file
3. Select File -> New -> Part -> Name the new part
4. Select one component from your master CATProduct File and copy it
5. Paste the component in a new part window
6. Repeat steps and until you have copied all of the components and pasted them as individual parts
7. Once you have the assembly completely separate into individual components, select File -> New Part
8. Copy each of the individual components from the working files and paste them into the new combined model file (the geometries of all of the parts should retain and align correctly in the combined part)
9. The new part is now ready to be exported as an STL file
10. Select Tools -> Generate CATPart from Product
11. Finally, Select File -> Salve As -> Save as type: STL

Tip: Occasionally some of the components may not align correctly in the combined part because of the way the original assembly was designed. To align parts, select Insert Menu -> Constraints Feature.
Before saving the file, it is advisable to review the settings that determine model accuracy and file size. To see these parameters:

1. Tools -> Options
2. In the Options dialog box, display the Performance tab
3. Under the General category (on the left), select Display
4. Review 3D Accuracy settings

Tip: Curves’ accuracy ratio: The higher the setting, the smoother the surface will be when dealing with complex geometries, especially if surfaces contain sudden small changes with small radii (like the bumps on a golf ball).

## IronCAD

1. Right-click on the part
2. Click Part Properties -> Rendering
3. Set Facet Surface Smoothing to 150
4. File -> Export
5. Select .STL

Note: IronCAD can export in many file formats depending on your geometry.
Tip: When working in assembly mode, you must save each of the component parts as individual STL files. The procedures for doing so are described below.
Saving a model design in STL format:

1. Open the model design in IronCAD.
2. Right-click on the part and select Part Properties -> Part dialog box
3. Make sure that the Rendering tab is displayed
4. Change the Surface Smoothness setting to an appropriate value for your model.
   1. If you have not established an appropriate value, try 150. The higher the number, the smoother the model surface will be.
   2. Change the Max Edge Length setting to an appropriate value for your model.
5. If you have not established an appropriate value, try 0.05. This setting produces good results, but increases file size and may require several minutes to render the model to STL format.
6. To create smoother model surfaces when designing spherical and torus geometries, select the Triangulated Mesh check box. Selecting this check box results in larger STL files, but may produce smoother curves in models. If the surfaces of the model design are planes, this setting does not improve the results.
7. Click OK to save the settings and close the dialog box.
8. File -> Export -> STL
9. In the Stereolithography dialog box, make sure PC is selected, and select the Binary Output check box.
10. Click OK to save the settings and create the STL file.

## Rhinoceros

1. Select Object
2. Mesh -> From a NURBS Object
3. Select Polygon Mesh -> Detailed Controls
4. Maximum aspect ratio: 2.0
5. Perspective -> Rendered View -> Observe smoothness and confirm it meets standards
6. To check that your mesh is uniform: Select the new object mesh -> Analyze -> Mass Properties -> Volume

### Rhinoceros 4

1. File -> Save As
2. Select File Type as STL
3. Select File Name -> Save
4. Select Binary
5. Select Detail Controls from Mesh Options
6. Max angle = 20, Max aspect ratio = 6, Min edge length = 0.0001
7. Click OK

Tip: Check your objects geometry and surface in the Object Properties tab to ensure object uniformity.

### Rhinoceros Version 3 and Later
Rhinoceros enables extensive control of STL properties when saving designs as STL files. Because Rhinoceros software is surface-based, the complete model design (even if an assembly) is saved as a single STL part.
Saving a model design in STL format

1. Select Part -> File -> Export Selected -> In the Save As Type box, select Stereolithography (``*.stl``)
2. Click Save
3. In the STL Mesh Export Options dialog box, set the STL tolerance – the maximum distance allowed between the surface of the design and the polygon mesh of the STL file.
   1. If you do not know the other settings appropriate for your model design, try these:
      1. Tolerance: Less than half of the printer’s resolution. For example, the setting shown in the figures above (0.01 mm) is a good setting for printing models at a resolution of 0.03 mm
      2. Maximum Angle: Default
      3. Maximum Aspect Ratio: Default
      4. Maximum Edge Length: Clear
      5. Maximum Edge Length: Clear
      6. Maximum Initial Grid Quads: Default
      7. Refine Mesh: Check
      8. Pack Textures: Check
      9. Click OK
         - In the STL Export Options dialog box, set the file type as Binary and click OK
           1. Note: If the Export open objects check box is selected, STL files will be created for each of the objects currently open. If this check box is cleared, an STL file is created for the selected object.

Important: STL files are suitable for 3D printing if the models they describe are “watertight”, that is, they do not contain holes or gaps. If an error message appears, click Cancel and fix the model design before saving it as an STL file. Steps for fixing mesh in Rhinoceros are detailed below.

**Troubleshooting Model Designs**
If a model design contains holes or gaps, it is not suitable for 3D printing. Before saving it as an STL file, you must make it “watertight.”

**To close holes and gaps in a model design:**

1. Check your object for errors: Command = Checknewobjects
2. Surface errors will display
3. Delete problem surfaces: Command = Selbad
4. Command: Rebuildedges

**Analyze Naked Edges:**

1. Analysis -> Show Edges/ Edges Off -> Command = Showedges
2. Select object -> Enter
3. Within dialogue box, select Naked Edges
   1. Highlighted lines are naked edges and must be joined to the rest of your model

**Fix Naked Edges**
Option 1:

1. Command = _Mesh
   1. This will create a mesh from the NURBS geometry (save your original NURBS file before doing this)
   2. Command = _Showedges
      1. This will detect naked edges
      2. Command = Fillhole
         - If you cannot find the Fillhole command, open your Tools tab and select Toolbar Layout
         - From the menu, check the box for Bonus Tools
         - The Bonus Tools window will open
         - Select Fill Mesh Hole
           1. If you have trouble, make sure you have the right updates installed

Option 2:

1. Click the Mesh from Surface/ Polysurface icon from toolbar
2. Polygon Mesh dialogue box will open
3. Click Detailed Control -> Polygon Mesh Detailed Options dialogue box will open
4. Enter desired settings -> OK
5. Select entire object
6. Tools menu -> Polygon Mesh -> Weld
7. Command = 180 for angle tolerance
   1. The Weld command will merge adjacent triangle points when 180 angle tolerance is set
8. Validate the object is watertight
9. Command = SelNakedMeshEdgePt
   1. If the resulting object contains holes or gaps, the mesh needs fixed
10. Repeat the Save As procedure

## PTC Creo

**3D printing in PolyJet:**

1. File -> Print -> 3D Print
2. Define Material
3. Define STL resolution
   1. Tip: Check your file for printability through the Printability Validation Tab

**Retired PTC Creo Formats: Pro/ENGINEER**

1. File -> Export -> Model
2. Set type to STL
3. Set chord height to 0. The field will be replaced by minimum acceptable value
4. Set Angle Control to 1
5. Click OK

Exporting your STL file can be done at all levels of design, for both individual parts and assemblies. When dealing with assemblies, you can specify parts of an assembly to either include or exclude from the resulting STL file. Use the procedure below for saving both parts and assemblies as STL files for eventual 3D printing.

**To save a Pro/E as an STL file:**

1. Check that the model design is continuous and “watertight”
   1. This step is especially important if the design was imported from a neutral design format because non-continuous bodies are likely to result in defective models
   2. To check for continuity:
      1. View the model with hidden lines displayed.
      2. From the View menu, select Display Setting -> Scheme -> PreWildfire. The model surfaces are displayed in magenta. If the design is continuous, the contour lines are white. If there are gaps, the lines are yellow.
      3. Fix the model design, if necessary, before saving it as an STL file.
      4. From the File menu, select Save a Copy. The Save a Copy dialog box appears.
      5. From the Type pull-down menu, select STL

**Deviation Control**
The Deviation Control settings in the Export STL dialog box affect the accuracy of the model and the size of its file.

1. Open Chord Height (chordal tolerance)
   1. This setting specifies the maximum distance between the surface of the original design and the tessellated surface of the STL triangle (the chord)
   2. Chord height controls the degree of tessellation of the model surface
   3. The smaller the chord height, the less deviation from the actual part surface (but the bigger the file)

**Angle Control**
This setting regulates how much additional tessellation occurs along surfaces with small radii. The smaller the radii, the more triangles are used. The setting can be between 0 and 1. Unless a higher setting is necessary, to achieve smoother surfaces, 0 is recommended.
Once you have reviewed the above the controls and adjusted your settings, click Apply -> OK to create the STL file.
**Saving a Pro/E Assembly as an STL File**

1. File -> Save a Copy
2. From the Type pull-down menu, select STL.
3. Export STL dialog box appears: Specify the parts of the assembly to either include or exclude within the resulting STL file
   1. Example: In the dialog box one of the parts of the assembly (the tire) has been excluded, leaving two parts (the hub and the main wheel) to be exported to the STL file. The design resulting from these settings (when you click OK) is shown on the left.
4. When you have made all of the required settings, click Apply and OK to create the STL file.

## Solid Edge ST6 - ST8

1. Application Button -> Save As (opens dialog box)
2. From the Save As drop down menu, select STL documents (`*.stl`)
3. Select the Options button from the Save As dialog box
4. Adjust Conversion Tolerance and Tolerance Units (millimeters recommended)
   1. The lower the conversation tolerance, the finer the tessellation
5. Adjust the Surface Plane Angle (dependent your desired surface smoothness)
   1. The lower the surface plane angle, the greater the accuracy (noticeable in small details)
      1. As a rule, the finer the tessellation and the greater the accuracy, the larger the size of the STL file, and the longer it takes to generate it
6. Under Output File as: Check Binary
   1. Binary STL files are much smaller than STL files saved in ASCII format
7. Click OK -> Save

Tip: Review the controls for exporting STL files in Solid Edge [here](https://docs.plm.automation.siemens.com/tdoc/se/107/help/#uid:index_importing_exporting_files:xid280320:xid727816:stlexp1d).

Note: Solid Edge is capable of creating individual STL files from the components of an assembly, but this functionality is not built into the program. It is achieved through the application programming interface (API), using Visual Basic scripts. This solution does not enable a visual preview of the polygon mesh before saving the STL files.
**Solid Edge (Older than ST6)**

1. Open model and select File -> Save As
2. Save As Type ->STL
3. Options -> Conversion Tolerance: 0.0254 mm for FDM; 0.015 mm for PolyJet
4. Set Surface Plane Angle to 45°
5. Select Binary type and OK
6. Name and Save STL file

Note: Solid Edge software from Siemens PLM (formerly USG) supports STL output at the core level, enabling you to save both parts and assemblies as STL files. However, when saving an assembly, all of its components are included in a single STL file.

## SolidWorks

1. File -> Save As
2. Set Save As Type to STL
3. Options -> Resolution -> Fine -> OK -> Save

**STL settings: How to change STL settings**

1. File -> Save As
2. STL -> Options
3. For a smoother STL file, change the Resolution to Custom
4. Change the deviation to 0.01 mm
5. Change the angle to 5 (smaller deviations and angles will produce a smoother file, but the file size will get larger)

Tip: Review file export options before you save your file from SolidWorks here.

**To save a model or a model assembly in STL Format:**

1. File -> Save As (Save As dialog box opens)
2. From the Save as type drop-down menu select STL (*.stl)
3. Click Options
4. The Export Options dialog box will display the file in a tessellated view
5. File Format selection is STL
6. In the Export Options dialog box -> Output As section select Binary
   1. The resulting file size will be much smaller than a file saved in ASCII format
7. In the Resolution section, select the appropriate option
   1. If you select Custom, you can manually adjust the Deviation and Angle settings
   2. The Deviation and Angle settings affect the tessellation of non-planar surfaces as follows:
      1. Lower deviation settings result in finer tessellation
      2. Lower angle settings result in greater accuracy, noticeable in small details
         - Note: The higher the resolution, the larger the size of the file, and the longer it takes to generate
8. For single material builds make sure that the following check box is selected: Save all components of an assembly in a single file
   1. This ensures that all components are saved as a single STL file.
9. For dual material builds (PolyJet) make sure that the following check box is NOT selected: Save all components of an assembly in a single file
   1. Note: Keep in mind that an assembly with many units will create many individual STL files when the “Save all components of an assembly in a single file” check box is left unchecked
10. Click OK
11. In the Save As dialog box, click Save
12. In the confirmation message, click Yes

## NX (Formerly UGS NX)

NX software from Siemens PLM (formerly USG), supports STL output at the core level, enabling you to save not only entire parts as STL files, but also selected surfaces of a part. This gives you great flexibility when preparing objects for 3D printing. In addition, assembly output enables you to save several components as a single unit while maintaining each component as a separate volume (shell).

1. File -> Export -> STL
2. Rapid Prototyping dialogue box will appear
3. Output Type: Binary
   1. Binary STL files are much smaller than STL files saved in ASCII format
4. Triangle Tolerance: 0.015 mm
   1. This is the maximum distance allowed between the surface of the original design and the tessellated surface of the STL triangle, and affects the smoothness of the model surface
5. Adjacency Tolerance: 0.015 mm
   1. This determines if two adjacent surfaces “attach”. If the distance between the two surfaces is less than this setting, they are considered attached. This setting must be less than the printing resolution. For example, when printing models at a resolution of 30 micrometers (microns), the setting must be no more than 0.03 mm.
6. Auto Normal Gen: Check box
7. Normal Display: Check box
8. Triangle Display: Check box
9. Click OK
10. Export Rapid Prototyping dialogue box will appear
11. Name your file and click OK

## Blender

Prior to exporting, ensure your object is uniform by checking that all surfaces/ vertices are connected.

**To check your file for uniformity:**

1. Enter Edit Mode, select your object, and press “L” over the mesh
   1. Areas that do not highlight are free-floating. All vertices must be connected for your part to print.
2. After you’ve confirmed your object is uniform, check for holes in the mesh of your part
3. Enter Edit Mode, deselect all vertices, and select Non Manifold from the drop down menu or simply hit Shft-Ctrl-Alt-M
4. Change the units and dimensions of your object
   1. Blender’s default measurement is called a Blender Unit and is equal to one meter
   2. Press “N” to bring up your dimensions tab
   3. Change units from Blender Units to Metric by selecting Properties -> Scene Tab
   4. Change units to Metric (preferably millimeter)
   5. Adjust your scale within the dimensions tab to compute with Metrics

Now your file is ready for export.

1. Select File -> Export as .STL (* .stl)

Tip: Modifiers can be applied during export or prior.

## ZBrush

ZBrush provides designers with incredible feature capabilities, however those features equate to thousands of tiny polygons that aren’t always feasible for 3D printing. To ensure your part is producible and that its details resolve as desired, download the Decimation Master Plugin from ZBrush.

The Decimation Master Plugin will allow you to optimize the polygon mesh of your part for printing by specifying a percentage of the poly mesh to preserve for export. It will preserve detail while reducing poly count. For a quick overview of the plugin, including masking to preserve areas where high poly count is critical for your model, click [here](https://www.youtube.com/watch?v=xTp6J644zGA).

Once you have optimized your part using the above steps, it is ready to export as an STL file.

1. Download the 3D Print Exporter Plugin from ZBrush
2. Select the ZPlugin menu
3. Click 3D Print Exporter
4. Define and scale your dimensions
5. Select STL -> STL Export
6. Save

## Maya

Maya is a free-form design space not specifically tailored to production, therefore it is especially crucial to check the dimensions and producibility of your design (are the wall thicknesses defined? Are all vertices connected?).

Check features for producibility:

1. Window -> Settings -> Preferences ->Settings
2. Change measurement units to millimeters
3. Review dimensions and scale within the Chanel Box
4. Finally, open Create -> Scene Assembly
5. Access measurement tools to check all feature sizes and thicknesses

Once you’ve checked your part for producibility, open the Rebuild Surface Options and define the surface density of your part. This will determine the resolution of the final 3D print. Check the design guidelines of your preferred technology to ensure the 3D print process can handle your desired resolution. Design guidelines on each 3D printing technology can be found here.

Now you’re ready to export.

1. Select File -> Export Selection -> Export as STL_DCE.



[原文链接](https://www.stratasysdirect.com/resources/tutorials/how-to-prepare-stl-files)