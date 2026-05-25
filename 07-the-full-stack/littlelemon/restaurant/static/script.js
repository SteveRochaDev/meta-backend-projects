const dateInput = document.getElementById('reservation_date');
const slotSelect = document.getElementById('reservation_slot');
const noBookings = document.getElementById('no-bookings');

const today = new Date().toISOString().split('T')[0];
dateInput.value = today;

const allSlots = [17, 18, 19, 20, 21];

async function loadBookings() {

    const date = dateInput.value;

    const response = await fetch(`/bookings/?date=${date}`);

    const bookings = await response.json();

    if (bookings.length === 0) {
        noBookings.textContent = 'No bookings for this date.';
    } else {
        noBookings.textContent = '';
    }

    slotSelect.innerHTML = '';

    allSlots.forEach(slot => {

        const option = document.createElement('option');

        option.value = slot;
        option.textContent = `${slot}:00`;

        const booked = bookings.some(
            booking => booking.reservation_slot === slot
        );

        if (booked) {
            option.disabled = true;
            option.textContent += ' (Booked)';
        }

        slotSelect.appendChild(option);
    });
}

dateInput.addEventListener('change', loadBookings);

loadBookings();