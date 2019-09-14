# FacialComposite_to_Photo
This is a implementation of the ***tensorflow 2.0 Pix2Pix implementation*** , trained to learn to translate facial composite into photos of real faces, given a facial composite sketch the Neural Network will be able to accurately predict a photograph of a face given a sketch.
This project has the potential of having a great commercial use in police related themes.

**Data-Preprocessing**
I used a combination of 4 different dataset's :
  -  CUHK student data set : http://mmlab.ie.cuhk.edu.hk/archive/facesketch.html
  -  Essex facial images collection:https://cswww.essex.ac.uk/mv/allfaces/index.html
  -  Faces Caltech 1999 Dataset: http://www.vision.caltech.edu/html-files/archive.html
  - Self-Made mini data set containing 50 images to sketches
  
to create a bigger one in order to train the Neural Network , only the first CUHK dataset contained real facial composite sketches so I created the function *create_sketch_from_image* to create "sketches" given the real face photos from the other 3 datasets.

Then I joined the facial composite sketches and the face photos with the *Concatenate whole Dataset* function to be able to place this on the ***tensorflow 2.0 Pix2Pix implementation*** bearly touching the implementations code as the nightly 2.0 version has a lot of bugs :)

Then separated the dataset into the corresponding train/test/val files and voila!

  - The old datasets are available on the datasets/old folder on the repository
  - The new datasets are available on the datasets/new folder on the repository
  - All of this functions are available on the function folder on the repository

**Training**

Training had no complication, I just plugged my self-made and customized dataset previously constructed to resamble the dataset of facades used on the tensorflow implementation. And trained this with 20 EPOCHS as my 4 year old GTX 1060 GB can't handle more running time without crushing and got some interesting results.

**Results**

**Conclusions**
As you can see results are quite impressive. The model has learned a very good mapping between sketches and faces. If this model had more data images and most importanly more trained epochs this model could achieve more than impressive results and be the state of the art implementations for facial composite , removing the use of facial composite software and increasing the chance of recognising criminals. On both cameras as it could be paired with face recognition, and the awareness of citizens towards the criminals would increase as they would have a face to compare to, therefore increasing the chance one more time of recognising this criminals.
