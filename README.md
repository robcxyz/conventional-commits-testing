# conventional-commits-testing

Testing repo for conventional commits release patterns and how to automatically maintain a changelog from commit messages. There are basically two schools of thought for auto-generating changelogs, from commit messages and from PRs. 

For commit message based changelogs, conventional commits will bump the version on each new `feat` flag. This can produce many incremented changes when you have lots of things that qualify as a feat and can result in many incremented versions to be released. This is especially true when practicing trunk based development. 

For PR based changelogs, every PR must be tagged which will then flow into the changelog. Pattern is to tag PR, squash commits, and merge from there to produce the release draft. 

Ideal solution would be to have something below a `feat` / `fix` that doesn't increment the semvar and is grouped within the release draft + changelog. Ideally commits would not increment the version automatically and all the `feats` / `fix` tags would just be grouped into the changelog / release draft. 

Would also accommodate PRs as well but they would need to follow the convention. 


### Labels 

- `feat` 
  - For features that should trigger a minor release 
- `feature` - TODO: ?
  - For features that should be grouped within a minor release 
- `fix`
  - For fixes that trigger a new patch 
- `refactor`
  - For changes in code style 

### GH Actions 

- https://github.com/bcoe/conventional-release-labels
  - Allows you to use custom labels 
- https://github.com/google-github-actions/release-please-action
  - Produces changelog and updates release draft
  - Has map for associating labels with 

###  Links 

- https://github.com/TimonVS/pr-labeler-action/issues/28
