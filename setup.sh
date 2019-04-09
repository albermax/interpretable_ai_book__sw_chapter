
# Make sure dependencies are handled in the right way
pip install --upgrade pip

# Download the repo and
# load the version the notebooks have been developed with.
git clone https://github.com/albermax/innvestigate.git
cd innvestigate/
git checkout tag/sw_chapter_snapshot

# Install the repo
python setup.py install

# Install TF
#pip install tensorflow
pip install tensorflow-gpu

# and other dependencies
pip install scikit-image matplotlib numpy scipy keras scikit-learn lime jupyter

# Download the sample images
cd examples/images
bash wget_imagenet_2011_samples.sh
cd ../../

# Copy notebooks into the right location
cp ../notebooks/* examples/notebooks

# Run Jupyter from inside the innvestigate folder examples/notebooks
jupyter notebook
