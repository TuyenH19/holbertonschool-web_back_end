export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => ({
      ...student,
      grade: (newGrades.find((grade) => grade.studentId === student.id) || { grade: 'N/A' }).grade,
    }));
}
