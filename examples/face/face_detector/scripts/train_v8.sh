#!/bin/sh
if ! test -f ../prototxt/face_train_v8.prototxt ;then
	echo "error: ../prototxt/face_train_v8.prototxt does not exit."
	echo "please generate your own model prototxt primarily."
        exit 1
fi
if ! test -f ../prototxt/face_test_v8.prototxt ;then
	echo "error: ../prototxt/face_test_v8.prototxt does not exit."
	echo "please generate your own model prototxt primarily."
        exit 1
fi
../../../../build/tools/caffe train --solver=../solver/solver_train_v8.prototxt -gpu 2 
#--snapshot=../snapshot/deepface_v8_iter_3083.solverstate
