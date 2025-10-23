Minimal example that crashes when cwltool splits files up in different directories.
This example has 2 steps:
1. Make `index.html` that refers `green.png` right next to it
2. Check if all the links in the HTML file are valid.

The second step fails when running under cwltool, as the files get put in separate folders. When running the python files normally, there is no error.

Forum post: https://cwl.discourse.group/t/output-files-not-next-to-each-other-in-next-step/1020/2

Test with this snippet:
```bash
git clone https://github.com/EmileSonneveld/cwl-example.git
pip install -q cwltool
export PATH="$PWD:$PATH"
cwltool generate-and-validate-files.cwl
```

Output:
```
INFO /usr/local/bin/cwltool 3.1.20250925164626
INFO Resolved 'generate-and-validate-files.cwl' to 'file:///src/generate-and-validate-files.cwl'
INFO [workflow ] start
INFO [workflow ] starting step generate_files_step
INFO [step generate_files_step] start
INFO [job generate_files_step] /tmp/cwj4myg7$ generate_files.py
INFO [job generate_files_step] completed success
INFO [step generate_files_step] completed success
INFO [workflow ] starting step gatherer_node_step
INFO [step gatherer_node_step] start
INFO [job gatherer_node_step] /tmp/_vhi9obs$ validate_files.py \
    /tmp/1256xx27/stgdcdca0a9-d3b3-4fce-884c-2ead38af24e5/index.html \
    /tmp/1256xx27/stg6e0ba83d-789c-4954-b0bb-4d11b450461a/green.png
Traceback (most recent call last):
  File "/src/validate_files.py", line 31, in <module>
    main(sys.argv[1:])
  File "/src/validate_files.py", line 19, in main
    raise Exception(f"File in img tag not found! {img_src}")
Exception: File in img tag not found! green.png
WARNING [job gatherer_node_step] exited with status: 1
WARNING [job gatherer_node_step] completed permanentFail
WARNING [step gatherer_node_step] completed permanentFail
INFO [workflow ] completed permanentFail
WARNING Final process status is permanentFail
```

With InitialWorkDirRequirement, the output is:
```
INFO /home/emile/openeo/venv_python3_8/bin/cwltool 3.1.20240708091337
INFO Resolved 'generate-and-validate-files.cwl' to 'file:///src/generate-and-validate-files.cwl'
INFO [workflow ] start
INFO [workflow ] starting step generate_files_step
INFO [step generate_files_step] start
INFO [job generate_files_step] /tmp/v0s22jg7$ generate_files.py
INFO [job generate_files_step] completed success
INFO [step generate_files_step] completed success
INFO [workflow ] starting step gatherer_node_step
INFO [step gatherer_node_step] start
INFO [job gatherer_node_step] /tmp/kkgd3cm2$ validate_files.py \
    /tmp/kkgd3cm2/index.html \
    /tmp/kkgd3cm2/green.png
File in img tag exists: green.png
Ok PNG: /tmp/kkgd3cm2/green.png
INFO [job gatherer_node_step] completed success
INFO [step gatherer_node_step] completed success
INFO [workflow ] completed success
{}INFO Final process status is success
```