gem "sentry-ruby" 
Sentry.init do |config|
  config.dsn = 'https://impressions.tk/'
  config.traces_sampler = lambda do |context|
    true
  end
