#!/usr/bin/env cwl-runner
cwlVersion: v1.0
$graph:
  - id: generate_files
    class: CommandLineTool
    baseCommand: "generate_files.py"
    inputs: [ ]
    outputs:
      generate_files_out:
        type: File[]
        outputBinding:
          glob: [ "index.html", "green.png" ]

  - id: validate_files
    class: CommandLineTool
    baseCommand: "validate_files.py"
    inputs:
      validate_files_in1:
        type: File[]
        inputBinding: { }
    outputs: [ ]

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
