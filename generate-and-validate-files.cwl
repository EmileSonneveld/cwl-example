#!/usr/bin/env cwl-runner
cwlVersion: v1.0
$graph:
  - id: generate_files
    class: CommandLineTool
    baseCommand: "generate_files.py"
    inputs: [ ]
    requirements:
      InlineJavascriptRequirement: {}
    outputs:
      generate_files_out:
        type: File
        secondaryFiles: $("green.png")
        outputBinding:
          glob: "index.html"

  - id: validate_files
    class: CommandLineTool
    baseCommand: "validate_files.py"
    inputs:
      validate_files_in1:
        type: File
        secondaryFiles: $("green.png")
    outputs: [ ]
    arguments:
     - $(inputs.validate_files_in1.path)
     - $(inputs.validate_files_in1.secondaryFiles[0])

  - id: main
    class: Workflow
    inputs: [ ]
    requirements:
      - class: SubworkflowFeatureRequirement
    steps:
      generate_files_step:
        in: [ ]
        out: [ generate_files_out ]
        run: "#generate_files"
      gatherer_node_step:
        in:
          validate_files_in1: generate_files_step/generate_files_out
        out: [ ]
        run: "#validate_files"
    outputs: [ ]
