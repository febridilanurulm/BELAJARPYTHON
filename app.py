from flask import Flask, request, jsonify
app = Flask(__name__)
tasks = [
    {"id":1,"tittle":"Belajar Python","done":False},
    {"id": 2, "title": "Mengerjakan Tugas", "done": False}
    ]

@app.route('/tasks',methods=['POST'])
def create_task():
    new_task = {
        "id":len(tasks) + 1,
        "tittle":request.json['title'],
        "done":False
    }
    tasks.append(new_task)
    return jsonify(new_task),201

@app.route('/tasks',methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})

@app.route('/tasks/<int:task_id>',methods=['GET'])
def get_task(task_id):
    task=next((task for task in tasks if task['id']==task_id),None)
    if task is None:
        return jsonify({'error':'Task not found'}),404
    return jsonify(task)

@app.route('/tasks/<int:task_id>',methods=['PUT'])
def update_task(task_id):
    task=next((task for task in tasks if task['id']==task_id),None)
    if task is None:
        return jsonify({'error':'Task not found'}),404
    task['title'] = request.json.get('title', task['title'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify(task)

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
    tasks.remove(task)
    return jsonify({'message': 'Task deleted'})

@app.route('/cobacoba',methods=['GET'])
def ucok():
    return tasks

if __name__ == '__main__':
    app.run(debug=True)