# Creat my blog

# Install Jekyll and Bundler gems through RubyGems
gem install jekyll bundler

# Download template:
https://github.com/williamcanin/typing-jekyll-template

# Build the site on the preview server
bundle exec jekyll serve

# Now browse to http://localhost:4000

# Deploy

- Change the _config.yml file according to the instruction :
```
baseurl: "" 
url: "https://rockkingjy.github.io"
```
- If it works quite well on local computer, using the commands:
```
bundle exec jekyll b
```

- Create an empty gitHub.io repository.

- Push the _site/ folder created by the local computer to the GitHub.io repository.

- Check the site created by GitHub page: https://rockkingjy.github.io
