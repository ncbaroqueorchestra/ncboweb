<style>
.ev-acc-card .card-header button {
  color: #272829;
  font-family: "Raleway", sans-serif;
  font-weight: 600;
  font-size: 0.92rem;
}
.ev-acc-card .card-header button:hover {
  color: #149ddd;
  text-decoration: none;
}
.ev-acc-card .card-header button:focus {
  box-shadow: none;
  text-decoration: none;
}
.ev-acc-card .card-header button .bx-chevron-down {
  transition: transform 0.25s ease;
  flex-shrink: 0;
}
.ev-acc-card .card-header button.collapsed .bx-chevron-down {
  transform: rotate(-90deg);
}
.ev-acc-date-badge {
  font-size: 0.75rem;
  background: #149ddd;
  color: #fff;
  border-radius: 4px;
  padding: 2px 8px;
  margin-right: 10px;
  white-space: nowrap;
  flex-shrink: 0;
}
.ev-acc-venue-inline {
  font-size: 0.82rem;
  color: #6c757d;
  margin-left: 8px;
}
.ev-acc-body-meta {
  font-size: 0.83rem;
  color: #6c757d;
  margin-bottom: 8px;
}
.ev-acc-body-desc {
  font-size: 0.88rem;
  margin-bottom: 12px;
}
.ev-acc-body-actions .btn {
  font-size: 0.78rem;
  margin-right: 6px;
}
</style>

<section id="events-accordion" class="section-bg">
  <div class="container">
    <div class="section-title">
      <h2>Upcoming Events</h2>
      <p>Browse &amp; Expand</p>
    </div>

    <div id="evAccordion">
      {% for event in site.data.events %}
        {% assign idx = forloop.index %}
        <div class="card ev-acc-card mb-2 border-0 shadow-sm">
          <div class="card-header bg-white border-0 p-0" id="evHead{{ idx }}">
            <button
              class="btn btn-block text-left d-flex align-items-center justify-content-between px-3 py-3{% unless forloop.first %} collapsed{% endunless %}"
              type="button"
              data-toggle="collapse"
              data-target="#evCollapse{{ idx }}"
              aria-expanded="{% if forloop.first %}true{% else %}false{% endif %}"
              aria-controls="evCollapse{{ idx }}">
              <div class="d-flex align-items-center flex-wrap" style="gap: 4px;">
                <span class="ev-acc-date-badge">{{ event.eventdate }}</span>
                <span>{{ event.heading }}</span>
                {% if event.venue %}
                  <span class="ev-acc-venue-inline d-none d-md-inline">&bull; {{ event.venue }}</span>
                {% endif %}
              </div>
              <i class="bx bx-chevron-down ml-3" style="font-size: 1.3rem;"></i>
            </button>
          </div>

          <div
            id="evCollapse{{ idx }}"
            class="collapse{% if forloop.first %} show{% endif %}"
            aria-labelledby="evHead{{ idx }}"
            data-parent="#evAccordion">
            <div class="card-body pt-1 pb-3 px-3">
              <div class="ev-acc-body-meta">
                <i class="bx bx-time-five"></i> {{ event.eventtime }}
                {% if event.venue %}
                  &nbsp;&bull;&nbsp;<i class="bx bx-building"></i> {{ event.venue }}
                {% endif %}
                {% if event.mapurl %}
                  &nbsp;&bull;&nbsp;<i class="bx bx-map-pin"></i>
                  <a href="{{ event.mapurl }}" target="_blank">{{ event.address }}</a>
                {% elsif event.address %}
                  &nbsp;&bull;&nbsp;<i class="bx bx-map-pin"></i> {{ event.address }}
                {% endif %}
              </div>
              <div class="ev-acc-body-desc">{{ event.description }}</div>
              <div class="ev-acc-body-actions">
                {% if event.ticketurl %}
                  <a class="btn btn-primary btn-sm" href="{{ event.ticketurl }}" target="_blank">Buy Tickets</a>
                {% endif %}
                {% if event.eventdetailsurl %}
                  <a class="btn btn-light btn-sm" href="{{ event.eventdetailsurl }}" target="_blank">More Details</a>
                {% endif %}
                {% if event.mapurl %}
                  <a class="btn btn-outline-secondary btn-sm" href="{{ event.mapurl }}" target="_blank"><i class="bx bx-directions"></i> Directions</a>
                {% endif %}
              </div>
            </div>
          </div>
        </div>
      {% endfor %}
    </div>
  </div>
</section>
