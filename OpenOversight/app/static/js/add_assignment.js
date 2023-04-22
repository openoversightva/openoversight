function set_jobs() {
  var dept_id = $('#dept').val();

  // fetch jobs for dept_id and modify #job_ids <select>
  var jobs_url = $('#add-assignment-form').data('jobs-url');
  var jobs = $.ajax({
    url: jobs_url,
    data: {department_id: dept_id}
  }).done(function(jobs) {
    //$('#job_title').replaceWith('<select id="job_title" name="job_title" required>');
    $("#job_title").empty()
    for (i = 0; i < jobs.length; i++) {
      $('select#job_title').append(
        $('<option></option>').attr("value", jobs[i][0]).text(jobs[i][1])
      );
    }
  });
  var units_url = $('#add-assignment-form').data('units-url');
  var units = $.ajax({
    url: units_url,
    data: {department_id: dept_id}
  }).done(function(units) {
    $('#unit').empty();
    for (i = 0; i < units.length; i++) {
      $('select#unit').append(
        $('<option></option>').attr("value", units[i][0]).text(units[i][1])
      );
    }
  });
}

$(document).ready(function() {
  set_jobs();
  $('select#dept').change(set_jobs);
});
