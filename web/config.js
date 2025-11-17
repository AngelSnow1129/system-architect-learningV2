// 系统架构设计师学习平台配置文件

const CONFIG = {
    // 考试类型配置
    examTypes: {
        architect: {
            name: '系统架构设计师',
            description: '软考高级资格考试',
            chapters: [
                { 
                    id: '00', 
                    name: '系统架构设计师第二版', 
                    stars: 5,
                    hasKeypoint: false,
                    hasMustKnow: false
                },
                { 
                    id: '01', 
                    name: '计算机硬件', 
                    stars: 4,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '02', 
                    name: '操作系统知识', 
                    stars: 5,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '03', 
                    name: '数据库系统', 
                    stars: 5,
                    hasKeypoint: true,
                    hasMustKnow: true
                },
                { 
                    id: '04', 
                    name: '嵌入式技术', 
                    stars: 3,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '05', 
                    name: '计算机网络', 
                    stars: 5,
                    hasKeypoint: true,
                    hasMustKnow: true
                },
                { 
                    id: '06', 
                    name: '其他计算机系统基础知识', 
                    stars: 3,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '07', 
                    name: '系统配置与性能评价', 
                    stars: 4,
                    hasKeypoint: false,
                    hasMustKnow: false,
                    altName: '系统安全分析与设计'
                },
                { 
                    id: '08', 
                    name: '信息系统基础知识', 
                    stars: 4,
                    hasKeypoint: false,
                    hasMustKnow: false,
                    altName: '系统可靠性'
                },
                { 
                    id: '09', 
                    name: '系统安全', 
                    stars: 4,
                    hasKeypoint: false,
                    hasMustKnow: false,
                    altName: '项目管理'
                },
                { 
                    id: '10', 
                    name: '软件工程', 
                    stars: 5,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '11', 
                    name: '面向对象技术', 
                    stars: 5,
                    hasKeypoint: true,
                    hasMustKnow: true
                },
                { 
                    id: '12', 
                    name: '项目管理', 
                    stars: 4,
                    hasKeypoint: true,
                    hasMustKnow: true,
                    altName: '数据结构与算法'
                },
                { 
                    id: '13', 
                    name: '系统架构设计', 
                    stars: 5,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '14', 
                    name: '软件可靠性基础', 
                    stars: 4,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '15', 
                    name: '软件架构的演化和维护', 
                    stars: 4,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '16', 
                    name: '未来信息综合技术', 
                    stars: 3,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '17', 
                    name: '补充-数学与经济管理', 
                    stars: 3,
                    hasKeypoint: true,
                    hasMustKnow: false
                },
                { 
                    id: '18', 
                    name: '补充-知识产权与标准化', 
                    stars: 3,
                    hasKeypoint: true,
                    hasMustKnow: false
                }
            ]
        }
    },

    // 视图类型配置
    viewTypes: {
        normal: {
            name: '完整章节',
            icon: '📖',
            folder: '',
            suffix: ''
        },
        keypoint: {
            name: '重点提纲',
            icon: '⭐',
            folder: 'keypoint',
            suffix: '_知识提纲'
        },
        mustknow: {
            name: '必背内容',
            icon: '🎯',
            folder: 'keypoint',
            suffix: '_必背补充'
        }
    },

    // 特殊文件映射（处理文件名不一致的情况）
    fileMapping: {
        keypoint: {
            '07': '07_系统安全分析与设计_知识提纲.md',
            '08': '08_系统可靠性_知识提纲.md',
            '09': '09_项目管理_知识提纲.md',
            '12': '12_数据结构与算法_知识提纲.md'
        },
        mustknow: {
            '12': '12_数据结构与算法_必背补充.md'
        }
    }
};

// 导出配置
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}
