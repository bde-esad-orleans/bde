module Jekyll
  class EventPageGenerator < Generator
    safe true
    priority :low

    def generate(site)
      # Générer les pages pour les événements
      site.collections['events'].docs.each do |event|
        site.pages << EventPage.new(site, site.source, event)
      end
      
      # Générer les pages pour les archives
      site.collections['archive'].docs.each do |event|
        site.pages << EventPage.new(site, site.source, event)
      end
    end
  end

  class EventPage < Page
    def initialize(site, base, event)
      @site = site
      @base = base
      # Enlever l'extension .md du nom
      clean_name = event.basename.gsub('.md', '')
      @dir = "#{event.collection.label}/#{clean_name}"
      @name = "index.html"
      
      self.process(@name)
      self.read_yaml(File.join(base, '_layouts'), 'event.html')
      
      # Copier les données de l'événement
      self.data.merge!(event.data)
      self.data['layout'] = 'event'
      self.content = event.content
    end
  end
end
