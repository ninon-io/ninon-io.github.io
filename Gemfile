# frozen_string_literal: true

source "https://rubygems.org"

# Static site generator. Built and deployed by .github/workflows/pages.yml.
gem "jekyll", "~> 4.4"

# Plugins the site actually uses.
group :jekyll_plugins do
  gem "jekyll-feed",          "~> 0.17"   # /feed.xml
  gem "jekyll-sitemap",       "~> 1.4"    # /sitemap.xml
  gem "jekyll-include-cache", "~> 0.2"    # caches repeated includes
  gem "jekyll-redirect-from", "~> 0.16" # legacy URL redirects
end

# Required on Ruby >= 3.4: these left the standard library.
gem "csv"
gem "base64"
gem "bigdecimal"
gem "logger"
gem "ostruct"

# Faster file watching on macOS during `bundle exec jekyll serve`.
gem "wdm", "~> 0.2", platforms: [:mingw, :x64_mingw, :mswin]
gem "http_parser.rb", "~> 0.6.0", platforms: [:jruby]
