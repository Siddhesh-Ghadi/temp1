# ```
#(C) Copyright IBM Corp.  2018. All Rights Reserved.
# ```
# 
# ```
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ```
# Load the data
import argparse

from sklearn.datasets import load_svmlight_file

defaultPath = "."
CLI=argparse.ArgumentParser()
CLI.add_argument(
   "--data_path",
   type=str,
   default=defaultPath
)

args = CLI.parse_args()

X,y = load_svmlight_file(args.data_path + "/HIGGS")

# Make the train-test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Convert to numpy ararys
import numpy as np
X_train = np.array(X_train.todense())
X_test  = np.array(X_test.todense())

# Normalize the training data
from sklearn.preprocessing import normalize
X_train = normalize(X_train, axis=1, norm='l1')
X_test  = normalize(X_test,  axis=1, norm='l1')

# Save the dense matrices
np.save(args.data_path + "/HIGGS.X_train", X_train)
np.save(args.data_path + "/HIGGS.X_test",  X_test)

# Save the labels
np.save(args.data_path + "/HIGGS.y_train", y_train)
np.save(args.data_path + "/HIGGS.y_test", y_test)
