
# Download the repo and
# load the version the notebooks have been developed with.
git clone https://github.com/albermax/innvestigate.git
cd innvestigate/
git checkout tags/1.0.7

# Install the repo
python setup.py install

# Install TF
#pip install tensorflow
pip install tensorflow-gpu

# and other dependencies
pip scikit-image matplotlib numpy scipy keras scikit-learn lime

# Download the sample images
cd examples/images
bash wget_imagenet_2011_samples.sh
cd ../../

# Copy notebooks into the right location
cp ../notebooks/* examples/notebooks
