from client import MultiFileGitWorkspaceDependencyDiffSynthesizerClient

def main():
    client = MultiFileGitWorkspaceDependencyDiffSynthesizerClient()
    res = client.synthesize_workspace_refactor_plan('Add Prometheus metrics exporter to all microservices')
    print('Multi-File Workspace Diff Synthesizer: ' + res['refactor_plan_id'])
    print('Mutation Sequence: ' + ' -> '.join(res['ordered_file_mutation_sequence']))
    print('Patch URL: ' + res['unified_diff_patch_manifest_url'])

if __name__ == '__main__':
    main()
