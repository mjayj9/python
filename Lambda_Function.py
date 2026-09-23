evaluate_student = lambda student: (
    f"[결과] {student.get('name', '무명')}: "
    f"최종점수 {sum(student.get('scores', [])) / len(student.get('scores', [1])):.1f}점 - "
    + (
        "수석 합격(A+)" if (sum(student.get('scores', [])) / len(student.get('scores', [1]))) >= 95
        else "우수 합격(A)" if (sum(student.get('scores', [])) / len(student.get('scores', [1]))) >= 90
        else "합격(B)" if (sum(student.get('scores', [])) / len(student.get('scores', [1]))) >= 80
        else "조건부 재시험(C)" if (sum(student.get('scores', [])) / len(student.get('scores', [1]))) >= 70
        else "과락(F)"
    )
    + f" | 비고: {'출석 미달' if student.get('attendance', 0) < 80 else '출석 정상'}"
)

# 실행 예시
student_data = {"name": "홍길동", "scores": [88, 92, 95], "attendance": 85}
print(evaluate_student(student_data))
# 출력: [결과] 홍길동: 최종점수 91.7점 - 우수 합격(A) | 비고: 출석 정상
