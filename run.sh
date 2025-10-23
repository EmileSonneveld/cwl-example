#!/bin/bash

export PATH="$PWD:$PATH"
cwltool --leave-tmpdir --strict generate-and-validate-files.cwl
