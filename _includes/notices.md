{% assign numNotices = 0 %}
    {% for notice in site.data.notices %}
        <div class="alert alert-primary d-flex align-items-center" role="alert" style="z-index:10000" data-aos="fade-in">
            <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Info:"><use xlink:href="#info-fill"/></svg>
        <div>
        {{ notice.message }}&nbsp;&nbsp;&nbsp;&nbsp;
        {% if notice.buttonText %}
            <a href="{{ notice.link }}" class="btn btn-primary">{{ notice.buttonText }}</a>
        {% endif %}
        </div>
        </div>
{% endfor %}