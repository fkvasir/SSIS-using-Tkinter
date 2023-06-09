require 'csv'
require 'shoes'

# Path to the CSV file
CSV_FILE_PATH = 'courses.csv'

# GUI Application
Shoes.app(title: 'Course Manager', width: 400, height: 300) do
  # Load courses from CSV file
  @courses = []
  CSV.foreach(CSV_FILE_PATH, headers: true) { |row| @courses << row['course_name'] }

  # Add courses to CSV file
  def add_courses(courses)
    CSV.open(CSV_FILE_PATH, 'a+') do |csv|
      courses.each do |course|
        csv << [course]
      end
    end
  end

  # Remove student from CSV file
  def remove_student(name)
    data = CSV.table(CSV_FILE_PATH)
    data.delete_if { |row| row[:name] == name }
    File.open(CSV_FILE_PATH, 'w') { |f| f.write(data.to_csv) }
  end

  # Edit student's name and course
  def edit_student(old_name, new_name, new_course)
    data = CSV.table(CSV_FILE_PATH)
    data.each do |row|
      if row[:name] == old_name
        row[:name] = new_name
        row[:course] = new_course
      end
    end
    File.open(CSV_FILE_PATH, 'w') { |f| f.write(data.to_csv) }
  end

  # GUI elements
  flow do
    para 'Enter student name:'
    @name_edit = edit_line
  end

  flow do
    para 'Select course:'
    @course_listbox = list_box items: @courses
  end

  button 'Add Student' do
    student_name = @name_edit.text.strip
    course_name = @course_listbox.text.strip

    if student_name.empty? || course_name.empty?
      alert('Please enter student name and select a course.')
    else
      CSV.open(CSV_FILE_PATH, 'a+') do |csv|
        csv << [student_name, course_name]
      end
      alert('Student added successfully!')
    end
  end

  button 'Remove Student' do
    student_name = @name_edit.text.strip

    if student_name.empty?
      alert('Please enter student name.')
    else
      remove_student(student_name)
      alert('Student removed successfully!')
    end
  end

  flow do
    para 'Enter new student name:'
    @new_name_edit = edit_line
  end

  flow do
    para 'Enter new course:'
    @new_course_listbox = list_box items: @courses
  end

  button 'Edit Student' do
    old_name = @name_edit.text.strip
    new_name = @new_name_edit.text.strip
    new_course = @new_course_listbox.text.strip

    if old_name.empty? || new_name.empty? || new_course.empty?
      alert('Please enter all fields.')
    else
      edit_student(old_name, new_name, new_course)
      alert('Student edited successfully!')
    end
  end
end
