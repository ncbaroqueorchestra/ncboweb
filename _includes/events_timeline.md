<style>
.ev-tl { position: relative; padding: 10px 0 20px; }
.ev-tl::before {
  content: '';
  position: absolute;
  left: 50%;
  top: 0; bottom: 0;
  width: 2px;
  background: #149ddd;
  transform: translateX(-50%);
}
.ev-tl-item {
  display: flex;
  justify-content: flex-end;
  padding: 0 calc(50% + 32px) 28px 0;
  position: relative;
}
.ev-tl-item.ev-tl-right {
  justify-content: flex-start;
  padding: 0 0 28px calc(50% + 32px);
}
.ev-tl-dot {
  position: absolute;
  left: 50%;
  top: 16px;
  width: 14px; height: 14px;
  background: #149ddd;
  border: 3px solid #f5f8fd;
  border-radius: 50%;
  box-shadow: 0 0 0 2px #149ddd;
  transform: translateX(-50%);
  z-index: 1;
}
.ev-tl-card {
  background: #fff;
  border-radius: 8px;
  padding: 18px 22px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
  width: 100%;
}
.ev-tl-date {
  font-size: 0.78rem;
  font-weight: 700;
  color: #149ddd;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 5px;
}
.ev-tl-card h5 { margin-bottom: 3px; font-size: 1rem; }
.ev-tl-venue { font-size: 0.83rem; color: #6c757d; margin-bottom: 8px; }
.ev-tl-card p { font-size: 0.88rem; margin-bottom: 10px; }
.ev-tl-card .btn { font-size: 0.78rem; margin-right: 4px; margin-top: 4px; }

@media (max-width: 767px) {
  .ev-tl::before { left: 16px; transform: none; }
  .ev-tl-item, .ev-tl-item.ev-tl-right {
    justify-content: flex-start;
    padding: 0 0 24px 44px;
  }
  .ev-tl-dot { left: 16px; transform: translateX(-50%); }
}
</style>

<section id="events" class="section-bg">
  <div class="container">
    <div class="section-title">
      <h2>Upcoming Events</h2>
      <p>Timeline</p>
    </div>
    <div class="ev-tl">
      {% for event in site.data.events %}
        <div class="ev-tl-item{% cycle '', ' ev-tl-right' %}">
          <div class="ev-tl-dot"></div>
          <div class="ev-tl-card">
            <div class="ev-tl-date">{{ event.eventdate }} &bull; {{ event.eventtime }}</div>
            <h5>{{ event.heading }}</h5>
            <div class="ev-tl-venue">
              {{ event.venue }}{% if event.address %}, {{ event.address }}{% endif %}
            </div>
            <p>{{ event.description }}</p>
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
      {% endfor %}
    </div>
  </div>
</section>
