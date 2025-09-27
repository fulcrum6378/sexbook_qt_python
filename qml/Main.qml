import QtQuick 6.9
import QtQuick.Controls 6.9
import "list"

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "Sexbook"

    FontLoader {
        id: normal
        source: "../assets/font/balsamiq_sans_regular.ttf"
    }

    Page {
        anchors.fill: parent
        background: Rectangle {
            anchors.fill: parent
            color: "#FFFBFF"
        }

        ListView {
            anchors.fill: parent
            model: reportListModel
            spacing: 8

            delegate: ReportItem {
                reportName: name
            }
        }
    }
}
