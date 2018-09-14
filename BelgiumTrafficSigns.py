

ROOT_PATH = '/Users/jay/github.com/jayasagar/traffic-sign-label-tensorflow'
train_data_dir = os.path.join(ROOT_PATH, "Training")
test_data_dir = os.path.join(ROOT_PATH, "Testing")

# Get all subdirectories of data_dir. Each represents a label.
directories = [d for d in os.listdir(train_data_dir)
               if os.path.isdir(os.path.join(train_data_dir, d))]
# Loop through the label directories and collect the data in
# two lists, labels and images.
labels = []
images = []
for d in directories:
    label_dir = os.path.join(train_data_dir, d)
    file_names = [os.path.join(label_dir, f)
                  for f in os.listdir(label_dir)
                  if f.endswith(".ppm")]
    for f in file_names:
        images.append(data.imread(f))
        labels.append(int(d))

