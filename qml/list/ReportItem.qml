import QtQuick 6.9
import QtQuick.Controls 6.9
import QtQuick.Shapes 1.9

Rectangle {
    id: reportItem
    property string reportName

    width: parent.width * 0.7
    height: 60
    anchors.horizontalCenter: parent.horizontalCenter
    color: "#FFD422"
    radius: 12

    Shape {
        id: clock

        width: 36
        height: 36
        anchors {
            left: parent.left
            leftMargin: (parent.height - height) / 2
            top: parent.top
            topMargin: (parent.height - height) / 2
        }

        ShapePath {
            fillColor: "#FFF"

            PathRectangle {
                width: clock.width
                height: clock.height
                radius: clock.width / 2
            }
        }
    }

    Shape {
        id: clockHour

        width: 4
        height: 12
        anchors {
            left: clock.left
            leftMargin: (clock.width - width) / 2
            top: clock.top
            topMargin: ((clock.height / 2) - height) + 1
        }
        transform: Rotation {
            origin.x: clockHour.width / 2
            origin.y: (clockHour.height) - 1
            angle: 90
        }

        ShapePath {
            fillColor: "#9A7C00"
            PathRectangle {
                width: clockHour.width
                height: clockHour.height
                radius: 1
            }
        }
    }

    TextEdit {
        text: parent.reportName
        anchors.centerIn: parent
        color: "#9A7C00"
        font.family: normal.font.family
        font.weight: normal.font.weight
        font.styleName: normal.font.styleName
        font.pixelSize: 18
    }
}
