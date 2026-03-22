<style>
.ev-ag-month {
  font-family: "Raleway", sans-serif;
  font-size: 1.1rem;
  font-weight: 800;
  color: #149ddd;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 24px 0 8px;
  border-bottom: 2px solid #149ddd;
  margin-bottom: 0;
}
.ev-ag-row {
  display: flex;
  align-items: flex-start;
  padding: 14px 0;
  border-bottom: 1px solid #e8eaed;
  gap: 20px;
}
.ev-ag-datecol {
  min-width: 70px;
  text-align: center;
  flex-shrink: 0;
}
.ev-ag-day {
  font-size: 2.1rem;
  font-weight: 700;
  line-height: 1;
  color: #272829;
  font-family: "Raleway", sans-serif;
}
.ev-ag-weekday {
  font-size: 0.72rem;
  text-transform: uppercase;
  color: #6c757d;
  letter-spacing: 0.06em;
}
.ev-ag-main { flex: 1; min-width: 0; }
.ev-ag-title { font-weight: 600; font-size: 1rem; font-family: "Open Sans", sans-serif; margin-bottom: 2px; }
.ev-ag-meta { font-size: 0.9rem; font-family: "Open Sans", sans-serif; color: #6c757d; margin-bottom: 5px; }
.ev-ag-desc { font-size: 1rem; font-family: "Open Sans", sans-serif; color: #444; margin-bottom: 7px; }
.ev-ag-actions .btn { font-size: 0.85rem; margin-right: 4px; }

@media (max-width: 575px) {
  .ev-ag-datecol { min-width: 52px; }
  .ev-ag-day { font-size: 1.6rem; }
  .ev-ag-row { gap: 12px; }
}
</style>

<section id="events">
  <div class="container">
    <div class="section-title">
      <h2>Upcoming Events</h2>
      <p>Agenda</p>
    </div>

    {% assign current_month = '' %}
    {% for event in site.data.events %}
      {% assign month_label = event.sortdate | date: "%B %Y" %}
      {% if month_label != current_month %}
        {% assign current_month = month_label %}
        <div class="ev-ag-month">{{ month_label }}</div>
      {% endif %}

      <div class="ev-ag-row">
        <div class="ev-ag-datecol">
          <div class="ev-ag-day">{{ event.sortdate | date: "%-d" }}</div>
          <div class="ev-ag-weekday">{{ event.sortdate | date: "%a" }}</div>
        </div>
        <div class="ev-ag-main">
          <div class="ev-ag-title">{{ event.heading }}</div>
          <div class="ev-ag-meta">
            {{ event.eventtime }}
            {% if event.venue %} &bull; {{ event.venue }}{% endif %}
            {% if event.mapurl %}
              &bull; <a href="{{ event.mapurl }}" target="_blank">{{ event.address }}</a>
            {% elsif event.address %}
              &bull; {{ event.address }}
            {% endif %}
          </div>
          <div class="ev-ag-desc">{{ event.description }}</div>
          <div class="ev-ag-actions">
            {% if event.ticketurl %}
              <a class="btn btn-primary btn-sm" href="{{ event.ticketurl }}" target="_blank">Buy Tickets</a>
            {% endif %}
            {% if event.eventdetailsurl %}
              <a class="btn btn-light btn-sm" href="{{ event.eventdetailsurl }}" target="_blank">More Details</a>
            {% endif %}
            {% if event.mapurl %}
              <a class="btn btn-outline-secondary btn-sm" href="{{ event.mapurl }}" target="_blank"><i class="bx bx-map-pin"></i> Map</a>
            {% endif %}
          </div>
        </div>
      </div>
    {% endfor %}
  </div>
</section>
